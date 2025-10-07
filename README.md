# Frontend Intelligence Knowledge Base

This repository is a monorepo containing a curated collection of powerful frontend libraries and tools. It serves as a knowledge base, with each sub-directory containing a specific project and a detailed `README.md` to explain its purpose, usage, and structure.

## How to Use This Repository

This repository contains sub-repositories that may be updated periodically. To ensure all local copies are up-to-date, you can run the provided Python script.

```bash
python3 update_repos.py
```
This script will iterate through all sub-directories, run `git pull` on any that are Git repositories, and then clean up their local `.git` folders to avoid conflicts with the parent monorepo.

## Contents

| Library/Tool  | Description                                                                                             | Details                                  |
|---------------|---------------------------------------------------------------------------------------------------------|------------------------------------------|
| `anime`       | A lightweight and powerful JavaScript animation engine.                                                 | [Read More](./anime/README.md)           |
| `axe-core`    | A lightweight, fast, and secure accessibility engine for automated web UI testing.                        | [Read More](./axe-core/README.md)        |
| `barba`       | A lightweight and flexible JavaScript library for creating smooth and fluid transitions between pages.    | [Read More](./barba/README.md)           |
| `bounce.js`   | A JavaScript library for creating beautiful and elegant CSS3-powered keyframe animations.                 | [Read More](./bounce.js/README.md)       |
| `draggable`   | A lightweight, modular, and accessible drag-and-drop library.                                           | [Read More](./draggable/README.md)       |
| `dynamics.js` | A JavaScript library designed to create realistic, physics-based animations.                            | [Read More](./dynamics.js/README.md)     |
| `lodash`      | A modern JavaScript utility library delivering modularity, performance, and extras.                     | [Read More](./lodash/README.md)          |
| `rellax`      | A buttery-smooth, super lightweight, vanilla JavaScript parallax library.                               | [Read More](./rellax/README.md)          |
| `velocity`    | A high-performance, standalone JavaScript animation engine.                                             | [Read More](./velocity/README.md)        |
| `waitanimate` | A web-based tool for adding a pause or delay between iterations of a looped CSS animation.                | [Read More](./waitanimate/README.md)     |