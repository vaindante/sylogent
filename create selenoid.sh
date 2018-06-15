#!/usr/bin/env bash
mkdir -p /etc/selenoid
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aerokube/cm selenoid start > /etc/selenoid/browsers.json
docker run -d --name selenoid -p 4444:4444 -v /etc/selenoid:/etc/selenoid:ro -v /var/run/docker.sock:/var/run/docker.sock aerokube/selenoid
docker run -d d--name selenoid -p 4444:4444 -v /var/run/docker.sock:/var/run/docker.sock -v `pwd`/config/:/etc/selenoid/:ro aerokube/selenoid:latest-release