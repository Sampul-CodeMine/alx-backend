#!/usr/bin/yarn dev
// Creating Redis Client with advanced Operations
import { createQueue } from 'kue';

const queue = createQueue({ name: 'push_notification_code' });
const job = queue.create('push_notification_code', {
  phoneNumber: '0123456789',
  message: 'Account is now active.'
});

job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
}).on('complete', () => {
  console.log('Notification job completed');
}).on('failed attempt', () => {
  console.log('Notification job failed');
}).save();
