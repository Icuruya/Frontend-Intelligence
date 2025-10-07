# Velocity.js

## Project Overview

Velocity.js is a high-performance, standalone JavaScript animation engine. It provides the same API as jQuery's `$.animate()` but with significantly better performance, making it ideal for complex UI animations and motion design. It features color animation, transforms, loops, easings, SVG support, and scrolling.

## Core Features

- **High-Performance Engine**: Outperforms traditional jQuery and CSS-based animations.
- **jQuery-Compatible API**: Can be used as a drop-in replacement for `$.animate()` in many cases.
- **Rich Animation Support**: Animates CSS properties, colors, transforms, and SVG attributes.
- **Advanced Control Flow**: Includes options for sequencing, looping, delaying, and queuing animations.
- **UI Pack**: An optional UI pack provides a suite of pre-made animations for showing, hiding, and grabbing attention.
- **Command-Based**: Offers a range of commands like `stop`, `pause`, `resume`, and `finish` for fine-grained control over animations.

## Installation & Setup

You can install Velocity.js via npm or include it directly from a CDN.

**NPM:**
```bash
npm install velocity-animate
```
Then, import it into your project:
```javascript
import Velocity from 'velocity-animate';
```

**CDN:**
```html
<script src="https://cdn.jsdelivr.net/npm/velocity-animate@2.0/velocity.min.js"></script>
```
If you want to use the UI pack for pre-made animations:
```html
<script src="https://cdn.jsdelivr.net/npm/velocity-animate@2.0/velocity.ui.min.js"></script>
```

## Key Concepts & Usage

Velocity can be called as a global function `Velocity(elements, ...)` or, if jQuery is present, chained like `$(elements).velocity(...)`.

### Example 1: Basic Property Animation

This example animates the `opacity` and `left` properties of an element.

**HTML:**
```html
<div id="my-element" style="position: relative; width: 100px; height: 100px; background: red;"></div>
```

**JavaScript:**
```javascript
const element = document.getElementById('my-element');

// Using the global function
Velocity(element, {
  opacity: 0.5,
  left: '200px'
}, {
  duration: 1000,
  easing: 'ease-in-out'
});
```

### Example 2: Chaining and Commands

This example demonstrates chaining multiple animation calls and using the `reverse` command.

**HTML:**
```html
<div id="chained-element" style="position: relative; width: 50px; height: 50px; background: green;"></div>
```

**JavaScript:**
```javascript
// This assumes jQuery or a similar library where Velocity has been patched.
// For vanilla JS, you would use nested callbacks or Promises.
$('#chained-element')
  .velocity({ translateX: '200px' }, { duration: 1000 })
  .velocity({ rotateZ: '90deg' }, { duration: 1000 })
  .velocity("reverse", { delay: 500 }); // Reverse the entire animation sequence
```

## Directory Structure

- **`src/`**: The core TypeScript source code for the animation engine.
- **`src-ui/`**: The source code for the optional UI Pack, which contains pre-made animation sequences.
- **`velocity.js` / `velocity.min.js`**: The compiled, distributable files for the main library.
- **`velocity.ui.js` / `velocity.ui.min.js`**: The compiled, distributable files for the UI pack.
- **`test/`**: Unit and integration tests for the library.
- **`legacy/`**: Contains older versions or compatibility files.