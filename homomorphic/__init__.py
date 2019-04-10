#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. module:: homomorphic
    :platform: Unix, Windows
    :synopsis: Homomorphic filtering module.

.. moduleauthor:: Nik Mohamad Aizuddin bin Nik Azmi <nik-mohamad-aizuddin@yandex.com>
"""

import numpy as np
from PIL import Image


def apply(img, **args):
    """
    Apply homormophic filter on an image

    High-frequency filters that are currently implemented:
        * butterworth
        * gaussian

    Paremters
    ---------
    img : np.ndarray
        Image in 2D numpy array format.
    alpha : float
        Float used to apply filter.
    beta : float
        Float used to apply filter.
    filter_type : str
        Type of filter to use. Can be either
            * 'butterworth'
            * 'gaussian'
    cutoff_freq : float
        Required for both butterworth and gaussian filters.
    order : float
        Required for butterworth filter only.
    """

    alpha = args.get('alpha', 0.75)
    beta = args.get('beta', 1.25)
    filter_type = args.get('filter_type', 'butterworth')
    cutoff_freq = args.get('cutoff_freq', 30)
    order = args.get('order', 2)

    # Take the image to log domain and then to frequency domain
    img_fft = np.fft.fft2(np.log1p(np.array(img, dtype="float")))

    if filter_type == 'butterworth':
        H = __butterworth_filter(img_fft.shape, cutoff_freq, order)
    elif filter_type == 'gaussian':
        H = __gaussian_filter(img_fft.shape, cutoff_freq)
    else:
        raise ValueError("Filter type should be either 'butterworth' or 'gaussian'")

    # Apply filter_type on frequency domain then take the image back to spatial domain
    img_fft_filt = __apply_filter(img_fft, H, alpha, beta)
    img_filt = np.fft.ifft2(img_fft_filt)
    img = np.exp(np.real(img_filt))-1
    return np.uint8(img)

def __butterworth_filter(img_shape, cutoff_freq, order):
    P = img_shape[0]/2
    Q = img_shape[1]/2
    U, V = np.meshgrid(range(img_shape[0]), range(img_shape[1]), sparse=False, indexing='ij')
    Duv = (((U-P)**2+(V-Q)**2)).astype(float)
    H = 1/(1+(Duv/cutoff_freq**2)**order)
    return 1 - H

def __gaussian_filter(img_shape, cutoff_freq):
    P = img_shape[0]/2
    Q = img_shape[1]/2
    H = np.zeros(img_shape)
    U, V = np.meshgrid(range(img_shape[0]), range(img_shape[1]), sparse=False, indexing='ij')
    Duv = (((U-P)**2+(V-Q)**2)).astype(float)
    H = np.exp((-Duv/(2*(cutoff_freq)**2)))
    return 1 - H

def __apply_filter(img, H, alpha, beta):
    H = np.fft.fftshift(H)
    img_filtered = (alpha + beta*H) * img
    return img_filtered
