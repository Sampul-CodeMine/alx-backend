#!/usr/bin/yarn dev
// Creating Redis Client with advanced Operations using Kue
import { createQueue, Job } from 'kue';

const BLACKLISTED_NUMS = ['4153518780', '4153518781'];
const queue = createQueue();

const sendNotification = (phoneNumber, message, job, done) => {
  const completed = 2;
  let undone = 2;
  const interval = setInterval(() => {
    if (completed - undone <= completed / 2) job.progress(completed - undone, completed);
    if (BLACKLISTED_NUMS.includes(phoneNumber)) {
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
      clearInterval(interval);
      return;
    }
    if (completed === undone) console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    --undone || done();
    undone || clearInterval(interval);
  }, 1000);
};

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
