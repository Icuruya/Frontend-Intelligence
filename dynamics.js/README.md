# dynamics.js

## Project Overview

Dynamics.js is a JavaScript library designed to create realistic, physics-based animations. It allows you to animate CSS properties, SVG attributes, and JavaScript object values using dynamic concepts like springs, gravity, and bounce, resulting in more natural and engaging motion.

## Core Features

- **Physics-Based Animation**: Implements various physics models like `spring`, `bounce`, and `gravity` for realistic motion.
- **Versatile Targeting**: Can animate CSS properties of DOM elements, SVG attributes, and values within any JavaScript object.
- **Multiple Animation Types**: Includes a variety of animation types, from `easeInOut` and `linear` to complex `bezier` curves.
- **Highly Customizable**: Each animation type offers specific parameters to fine-tune its behavior, such as `frequency`, `friction`, and `bounciness`.
- **Built-in Utilities**: Provides its own `dynamics.setTimeout` to prevent issues with `requestAnimationFrame` in background tabs, and a debug mode to slow down animations for easier tweaking.

## Installation & Setup

You can install Dynamics.js via npm, Bower, or by including it directly from a CDN or local file.

**NPM:**
```bash
npm install dynamics.js
```

**Bower:**
```bash
bower install dynamics.js
```

**CDN/Direct Include:**
```html
<script src="https://unpkg.com/dynamics.js/lib/dynamics.min.js"></script>
```

## Key Concepts & Usage

The library's main function is `dynamics.animate()`, which applies a physics-based animation to a target.

### Example 1: Spring Animation on a DOM Element

This example applies a `spring` animation to an element, causing it to "spring" to its new position with a bounce effect.

```html
<div id="my-element" style="width: 100px; height: 100px; background: blue;"></div>

<script>
  const el = document.getElementById('my-element');

  dynamics.animate(el, {
    translateX: 300,
    rotateZ: 45
  }, {
    type: dynamics.spring,
    frequency: 200,
    friction: 250,
    duration: 1500
  });
</script>
```

### Example 2: Animating SVG Path Attributes

This example demonstrates animating the `d` attribute of an SVG path to morph its shape, along with its fill color.

```html
<svg width="200" height="200">
  <path id="my-path" d="M10,10 L10,190 L190,100 Z" fill="red"></path>
</svg>

<script>
  const path = document.getElementById('my-path');

  dynamics.animate(path, {
    d: "M10,10 L190,10 L100,190 Z", // Target shape
    fill: "#00FF00"
  }, {
    type: dynamics.bounce,
    duration: 2000
  });
</script>
```

## Directory Structure

- **`src/`**: Contains the core source code of the library, written in CoffeeScript.
- **`lib/`**: (This directory is not in the source but is created on build) Contains the compiled and minified JavaScript files (`dynamics.js`, `dynamics.min.js`).
- **`test/`**: Unit tests for the library, written for Mocha and Chai.
- **`package.json`**: Defines project metadata, dependencies, and build scripts.