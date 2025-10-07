# Bounce.js

## Project Overview

Bounce.js is a JavaScript library for creating beautiful and elegant CSS3-powered keyframe animations. It provides a simple API to build complex animations by chaining together effects like scale, rotate, translate, and skew. The library can be used to either generate static CSS keyframes or to apply animations to DOM elements dynamically.

## Core Features

- **Chainable Animation Components**: Build complex animations by chaining `scale`, `rotate`, `translate`, and `skew` methods.
- **Pre-defined Easing Effects**: Includes a set of easing options like "bounce", "sway", and "hardbounce" to create lively animations.
- **Customizable Physics**: Fine-tune animations by adjusting parameters like duration, delay, bounces, and stiffness.
- **Static & Dynamic Usage**: Can be used to define named CSS animations for use in stylesheets or apply animations directly to elements with JavaScript.
- **No Dependencies**: A standalone library with no external dependencies for its core functionality.

## Installation & Setup

You can install Bounce.js via npm or Bower.

**NPM:**
```bash
npm install bounce.js
```

**Bower:**
```bash
bower install bounce.js
```

After installation, you can include the library in your project.

```html
<script src="path/to/bounce.min.js"></script>
```

## Key Concepts & Usage

The core of the library is the `Bounce` object, which you use to build and apply your animations.

### Example 1: Simple Rotation Animation

This example creates a simple animation that rotates an element 90 degrees and defines it as a named CSS animation called `my-animation`.

```javascript
// 1. Create a new Bounce object
var bounce = new Bounce();

// 2. Build the animation
bounce.rotate({
  from: 0,
  to: 90,
  duration: 1000,
  stiffness: 3
});

// 3. Define the animation for CSS use
bounce.define("my-animation");
```
You can then use this animation in your CSS:
```css
.my-element {
  animation: my-animation 1s linear both;
}
```

### Example 2: Chained Animation Applied Directly

This example creates a more complex, multi-stage animation and applies it directly to all elements with the class `.animation-target`.

```javascript
// 1. Create a new Bounce object
var bounce = new Bounce();

// 2. Build the animation by chaining methods
bounce
  .translate({
    from: { x: -100, y: 0 },
    to: { x: 0, y: 0 },
    duration: 600,
    stiffness: 4
  })
  .scale({
    from: { x: 1, y: 1 },
    to: { x: 0.5, y: 1.5 },
    easing: "sway",
    duration: 800,
    stiffness: 2
  })
  .scale({
    from: { x: 1, y: 1},
    to: { x: 2, y: 1 },
    easing: "sway",
    duration: 300
  });

// 3. Apply the animation directly to elements
bounce.applyTo(document.querySelectorAll(".animation-target"));
```

## Directory Structure

- **`app/`**: Contains the core source code of the library, written in CoffeeScript.
- **`test/`**: Unit tests for the library, written using Mocha and Chai.
- **`dist/`**: (This directory is not in the source but is created on build) Contains the compiled `bounce.js` and `bounce.min.js` files.
- **`Gruntfile.coffee`**: The configuration file for the Grunt build system, used to compile and test the project.