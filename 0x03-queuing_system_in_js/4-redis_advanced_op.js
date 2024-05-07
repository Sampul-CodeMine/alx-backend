#!/usr/bin/yarn dev
// Creating Redis Client with advanced Operations
import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.toString()}`);
});

const hashUpdate = (hashArg, fieldName, fieldValue) => {
  client.HSET(hashArg, fieldName, fieldValue, print);
};

const displayHash = (hashArg) => {
  client.HGETALL(hashArg, (_err, data) => console.log(data));
};

client.on('connect', () => {
  console.log('Redis client connected to the server');
  runner();
});

function runner () {
  const hashObject = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2
  };
  for (const [key, val] of Object.entries(hashObject)) {
    hashUpdate('HolbertonSchools', key, val);
  }
  displayHash('HolbertonSchools');
}
