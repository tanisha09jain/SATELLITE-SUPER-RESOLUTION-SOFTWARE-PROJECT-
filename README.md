# SATELLITE-SUPER-RESOLUTION-SOFTWARE-PROJECT-
# Satellite Image Super-Resolution

## Project Overview

This project investigates deep learning based super-resolution
techniques for improving the spatial quality of satellite images.

The objective is to reconstruct a high-resolution satellite image
from a low-resolution input while preserving important spatial
details.

## Problem Statement

Satellite imagery may have limited spatial resolution, making
fine details such as buildings, roads and boundaries difficult
to identify.

Image super-resolution attempts to reconstruct a higher-resolution
image from a lower-resolution input.

## Objectives

- Study existing satellite image super-resolution techniques.
- Prepare a satellite image dataset.
- Generate 4× low-resolution images from high-resolution images.
- Establish bicubic interpolation as a baseline.
- Evaluate a pretrained Real-ESRGAN model.
- Compare reconstruction quality using PSNR and SSIM.
- Investigate Transformer/GAN-based approaches for future work.

## Methodology

High Resolution Image
        ↓
4× Downsampling
        ↓
Low Resolution Image
        ↓
┌───────────────────────┐
│ Bicubic Baseline      │
│ Real-ESRGAN Baseline  │
└───────────────────────┘
        ↓
Super-Resolved Image
        ↓
PSNR / SSIM Evaluation
        ↓
Comparison

## Dataset

A satellite image super-resolution dataset is being used for
the experiments.

The initial experiments will use a smaller subset of the dataset
before scaling to the complete dataset.

## Models

### Baseline
Bicubic interpolation

### Deep Learning Baseline
Real-ESRGAN

### Proposed Direction
Swin Transformer + GAN based super-resolution approach

## Evaluation Metrics

- PSNR
- SSIM

## Current Progress

- Problem identification completed
- Dataset identified
- Project repository created
- Literature review started
- Dataset preprocessing pipeline being developed
- 4× degradation pipeline being developed
- Bicubic baseline being established
- Real-ESRGAN baseline planned
- Quantitative evaluation using PSNR and SSIM planned

## Future Work

- Complete preprocessing
- Run experiments on multiple satellite images
- Evaluate Real-ESRGAN
- Implement Transformer/GAN based architecture
- Compare models quantitatively and visually
- Analyze limitations and future improvements
