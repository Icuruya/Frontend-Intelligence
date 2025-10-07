# Rellax.js

## Project Overview

Rellax is a buttery-smooth, super lightweight, vanilla JavaScript parallax library. It allows you to create parallax scrolling effects on elements with a simple setup and a minimal performance footprint. It works on both desktop and mobile devices.

## Core Features

- **Lightweight & Performant**: A small file size with no dependencies, ensuring it doesn't slow down your site.
- **Simple Declarative API**: Parallax effects are controlled through simple `data-` attributes in your HTML.
- **Customizable Speed**: Easily control the speed and direction of parallax elements.
- **Responsive Speeds**: Set different parallax speeds for different screen sizes (mobile, tablet, desktop).
- **Centering Options**: Can be configured to keep parallax elements centered in the viewport.
- **Horizontal & Vertical Support**: Supports both vertical and horizontal parallax scrolling.
- **Custom Wrapper Support**: Can be configured to track the scroll position of a specific container instead of the `body`.

## Installation & Setup

You can install Rellax via npm or include it directly from a CDN.

**NPM:**
```bash
npm install rellax
```

**CDN:**
```html
<script src="https://cdn.jsdelivr.net/gh/dixonandmoe/rellax@master/rellax.min.js"></script>
```

After including the script, you need to initialize it.

## Key Concepts & Usage

To use Rellax, add the class you intend to target (e.g., `.rellax`) to your HTML elements and then create a new `Rellax` instance in your JavaScript.

### Example 1: Basic Usage with Different Speeds

This example demonstrates how to apply different parallax speeds to elements. A negative speed makes the element move slower than the scroll, while a positive speed makes it move faster.

**HTML:**
```html
<div class="rellax" data-rellax-speed="-2">Slower</div>
<div class="rellax" data-rellax-speed="7">Faster</div>
<div class="rellax" data-rellax-speed="0">No effect</div>
```

**JavaScript:**
```javascript
// Initialize Rellax on all elements with the 'rellax' class
var rellax = new Rellax('.rellax');
```

### Example 2: Centered, Horizontal Parallax

This example shows how to configure Rellax to create a horizontal parallax effect and keep the elements centered.

**HTML:**
```html
<div class="rellax-horizontal" data-rellax-speed="3" data-rellax-percentage="0.5">
  Item 1
</div>
<div class="rellax-horizontal" data-rellax-speed="-3" data-rellax-percentage="0.5">
  Item 2
</div>
```

**JavaScript:**
```javascript
// Initialize Rellax with options
var rellax = new Rellax('.rellax-horizontal', {
  horizontal: true, // Enable horizontal mode
  center: true      // Center elements
});
```

## Directory Structure

- **`rellax.js`**: The full, unminified source code of the library.
- **`rellax.min.js`**: The minified version of the library, suitable for production use.
- **`demo.html`**: A demonstration page showcasing the library's features.
- **`tests/`**: Contains HTML files for testing various features and configurations.
- **`package.json`**: Defines project metadata and dependencies.