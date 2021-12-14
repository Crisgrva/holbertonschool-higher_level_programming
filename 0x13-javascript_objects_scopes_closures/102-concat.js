#!/usr/bin/node
const { argv } = require('process');
const fs = require('fs');

const [fd1, fd2, fd3] = [argv[2], argv[3], argv[4]];

const content1 = fs.readFileSync(fd1, 'utf-8');
const content2 = fs.readFileSync(fd2, 'utf-8');

fs.writeFileSync(fd3, content1 + content2);
