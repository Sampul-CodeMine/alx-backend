#!/usr/bin/yarn dev
// Creating Redis Client with advanced Operations using Kue
import { Queue, Job } from 'kue';

const createPushNotificationsJobs = (jobs, queue) => {
  if (jobs instanceof Array) {
    for (const jobObj of jobs) {
      const job = queue.create('push_notification_code_3', jobObj);
      job.on('enqueue', () => {
        console.log(`Notification job created: ${job.id}`);
      }).on('complete', () => {
        console.log(`Notification job ${job.id} completed`);
      }).on('failed', (error) => {
        console.log(`Notification job ${job.id} failed: ${error.message || error.toString()}`);
      }).on('progress', (progress, data) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      }).save();
    }
  } else {
    throw new Error('Jobs is not an array');
  }
};

export default createPushNotificationsJobs;
module.exports = createPushNotificationsJobs;
