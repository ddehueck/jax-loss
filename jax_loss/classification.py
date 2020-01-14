import jax.numpy as np


def bce_w_logits(x, y, weight=None, average=True):
    """
    Binary Cross Entropy Loss
    Should be numerically stable, built based on: https://github.com/pytorch/pytorch/issues/751

    :param x: Input tensor
    :param y: Target tensor
    :param weight: Vector of example weights
    :param average: Boolean to average resulting loss vector
    :return: Scalar value
    """
    max_val = np.clip(x, 0, None)
    loss = x - x * y + max_val + np.log(np.exp(-max_val) + np.exp((-x - max_val)))

    if weight is not None:
        loss = loss * weight

    if average:
        return loss.mean()
    else:
        return loss.sum()
