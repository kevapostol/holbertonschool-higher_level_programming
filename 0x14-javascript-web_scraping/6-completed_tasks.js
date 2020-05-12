#!/usr/bin/node
const request = require('request');
const uri = process.argv[2];
request.get(uri, (error, response, body) => {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const completedTasks = {};
    for (const task of JSON.parse(body)) {
      if (task.completedTasks === true) {
        if (!(task.userId in completedTasks)) {
          completedTasks[task.userId] = 1;
        } else {
          completedTasks[task.userId] += 1;
        }
      }
    }
    console.log(completedTasks);
  }
});
