#!/usr/bin/yarn dev
// Creating Redis Client with advanced Operations
import { createClient } from 'redis';

const client = createClient();
const KILL_SERVER = 'KILL_SERVER';

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.toString()}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.subscribe('holberton school channel');

client.on('message', (_err, data) => {
  console.log(data);
  if (data === KILL_SERVER) {
    client.unsubscribe();
    client.quit();
  }
});
