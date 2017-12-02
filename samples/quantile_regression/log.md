# 2017-12-02

Experiments with loss

## MSE
Raw mse loss: 71297f56d8a2dc3aa80b986effd7e5be854ebc18, run Dec02_12-31-57_gpu-pong-qr-mse

Converge, but not very fast

## Huber loss without multipliers

c3620ebf8ab81fe5bfbb5502f9419f72614d5bf3, run Dec02_12-46-13_gpu-pong-qr-huber

Convergence is better.

## Quantile regression as in paper

Implement quantile regression as in paper: loss is scaled with tau-dirac{u < 0}

2e3e814acb527ce0237d96b75f22f3091468fb47, run Dec02_13-11-56_gpu-pong-qr-qr-paper

Not converging, tails are huge, Q-values are wrong

## Quantile regression fixed

Implement QR with penalization fixed: loss is scaled with tau - dirac{u > 0}

e9f811f809cc9498bd69dc56446b4a22a4bbddcc, run Dec02_13-13-51_gpu-pong-qr-qr-fixed

Not converging, tails are huge, Q-values are wrong.

ed272209e40b92c2ca74086e96b9d494cbfba797, run Dec02_13-21-55_gpu-pong-qr-qr-fixed-2