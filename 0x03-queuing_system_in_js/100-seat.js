#!/usr/bin/yarn dev
import express from 'express';
import { promisify } from 'util';
import { createQueue } from 'kue';
import { createClient } from 'redis';

const app = express();
const client = createClient({ name: 'reserve_seat' });
const queue = createQueue();
const RESERVED_SEATS = 50;
const PORT = 1245;
let reservationEnabled = false;

async function resetAvailableSeats (initialSeatsCount) {
  return promisify(client.SET).bind(client)('available_seats', Number.parseInt(initialSeatsCount));
}

/**
 * Function to reserve seats or modify the seats reserved
 * @param {number} number: number of seats to reserve
 */
async function reserveSeat (number) {
  return promisify(client.SET).bind(client)('available_seats', number);
}

/**
 * Function to retrieve the number of seats reserved or available
 */
async function getCurrentAvailableSeats () {
  return promisify(client.GET).bind(client)('available_seats');
}

/**
 * This is the route to get available number of seats not reserved
 */
app.get('/available_seats', (_, response) => {
  getCurrentAvailableSeats().then((numberOfAvailableSeats) => {
    response.json({ numberOfAvailableSeats });
  });
});

/**
 * This is a route to request for seat(s) reservation
 */
app.get('/reserve_seat', (req, response) => {
  if (reservationEnabled === true) {
    try {
      const job = queue.create('reserve_seat');
      job.on('failed', (error) => {
        console.log(`Seat reservation job ${job.id} failed: ${error.message || error.toString()}`);
      }).on('complete', () => {
        console.log(`Seat reservation job ${job.id} completed`);
      }).save();
      response.json({ status: 'Reservation in process' });
    } catch {
      response.json({ status: 'Reservation failed' });
    }
  } else {
    return response.json({ status: 'Reservations are blocked' });
  }
});

/**
 * This is a route to process request for seat reservation
 */
app.get('/process', (req, response) => {
  response.json({ status: 'Queue processing' });
  queue.process('reserve_seat', (job, done) => {
    getCurrentAvailableSeats()
      .then((data) => Number.parseInt(data || 0))
      .then((seatsAvailable) => {
        reservationEnabled = seatsAvailable <= 1 ? false : reservationEnabled;
        if (seatsAvailable >= 1) {
          reserveSeat(seatsAvailable - 1).then(() => done());
        } else {
          done(new Error('Not enough seats available'));
        }
      });
  });
});

app.listen(PORT, () => {
  resetAvailableSeats(process.env.RESERVED_SEATS || RESERVED_SEATS)
    .then(() => {
      reservationEnabled = true;
      console.log(`API server listening on port ${PORT}`);
    });
});

export default app;
module.exports = app;
