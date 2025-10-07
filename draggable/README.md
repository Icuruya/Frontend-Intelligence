# @shopify/draggable

## Project Overview

`@shopify/draggable` is a lightweight, modular, and accessible drag-and-drop library. It provides a comprehensive API to create a fully customized drag-and-drop experience by abstracting away native browser events. The library is designed to be extended with modules for different behaviors like sorting, swapping, and dropping.

## Core Features

- **Modular Design**: A core `Draggable` engine with optional modules (`Sortable`, `Droppable`, `Swappable`) for specific behaviors.
- **Extensive Event System**: A rich set of events (`drag:start`, `sortable:sort`, `drag:stop`, etc.) provides deep control over the user experience.
- **Sensor-Based**: Works with native mouse, touch, and force touch events through a sensor-based architecture.
- **Accessibility Focused**: Includes plugins for accessibility, such as live announcements for screen readers.
- **Framework Agnostic**: A plain JavaScript library that can be used with any framework.
- **Plugin System**: Extend functionality with plugins for features like scroll-on-drag, snapping, and collision detection.

## Installation & Setup

You can install Draggable via npm or include it directly from a CDN.

**NPM:**
```bash
npm install @shopify/draggable
```
Then, import the modules you need:
```javascript
import { Draggable, Sortable } from '@shopify/draggable';
```

**CDN:**
```html
<script type="module">
  import { Draggable, Sortable } from 'https://cdn.jsdelivr.net/npm/@shopify/draggable/build/esm/index.mjs';
</script>
```

## Key Concepts & Usage

The library is initialized by creating an instance of `Draggable` or one of its modules, passing in the container elements and a set of options.

### Example 1: Basic Draggable

This example makes all elements with the class `.item` inside a `.container` draggable.

**HTML:**
```html
<div class="container">
  <div class="item">Item 1</div>
  <div class="item">Item 2</div>
  <div class="item">Item 3</div>
</div>
```
**JavaScript:**
```javascript
import { Draggable } from '@shopify/draggable';

const container = document.querySelector('.container');

const draggable = new Draggable(container, {
  draggable: '.item' // The selector for draggable elements
});

// --- Event Listeners ---
draggable.on('drag:start', (evt) => {
  console.log('drag:start', evt);
});

draggable.on('drag:stop', (evt) => {
  console.log('drag:stop', evt);
});
```

### Example 2: Sortable List

The `Sortable` module builds on `Draggable` to provide list-sorting capabilities.

**HTML:**
```html
<ul class="sortable-list">
  <li>Item 1</li>
  <li>Item 2</li>
  <li>Item 3</li>
</ul>
```
**JavaScript:**
```javascript
import { Sortable } from '@shopify/draggable';

const list = document.querySelector('.sortable-list');

const sortable = new Sortable(list, {
  draggable: 'li' // Draggable elements are list items
});

// --- Event Listeners ---
sortable.on('sortable:start', (evt) => {
  console.log('sortable:start', evt);
});

sortable.on('sortable:sort', (evt) => {
  console.log('sortable:sort', evt);
});

sortable.on('sortable:stop', (evt) => {
  console.log('sortable:stop', evt);
});
```

## Directory Structure

- **`src/`**: Contains the core source code, organized by module (`Draggable`, `Sortable`, `Droppable`, `Swappable`).
- **`src/Draggable/`**: The main engine, including its event system, plugins, and sensors.
- **`src/Plugins/`**: Contains plugins that can be shared across different modules (e.g., `Collidable`, `Snappable`).
- **`examples/`**: A full project with live examples demonstrating various features.
- **`doc/`**: Contains additional documentation, including a guide for using Draggable with TypeScript.
- **`test/`**: Unit and integration tests for the library.