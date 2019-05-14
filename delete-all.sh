#!/bin/bash

kubectl delete service service-hacker service-victim service-server

kubectl delete networkpolicy arpspoof-internal arpspoof-public

kubectl delete pod hacker victim server

