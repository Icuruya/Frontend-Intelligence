# Barba.js

## Project Overview

Barba.js is a lightweight and flexible JavaScript library for creating smooth and fluid transitions between your website's pages. It uses PJAX (pushState + Ajax) to turn your website into a Single Page Application (SPA), which reduces page load delays, minimizes HTTP requests, and enhances the user experience.

## Core Features

- **SPA-like Navigation**: Fetches pages in the background without a full page refresh.
- **Transition Control**: A powerful hook-based system (`leave`, `enter`, etc.) to control animations between pages.
- **Smart Prefetching**: Can prefetch pages on hover to make navigation feel instantaneous.
- **Routing System**: Select different transitions based on page-specific rules (e.g., by namespace or route).
- **Cache Support**: Caches previously visited pages to speed up subsequent visits.
- **Modular Architecture**: Composed of a core engine with optional plugins like `@barba/css`, `@barba/prefetch`, and `@barba/router`.

## Installation & Setup

You can install Barba.js via npm or include it directly from a CDN.

**NPM:**
```bash
npm install @barba/core
```
Then, import and initialize it in your project:
```javascript
import barba from '@barba/core';

barba.init({
  // options
});
```

**CDN:**
```html
<script src="https://cdn.jsdelivr.net/npm/@barba/core"></script>
<script>
  barba.init({
    // options
  });
</script>
```

## Key Concepts & Usage

### 1. HTML Markup

Barba requires a specific HTML structure to identify which parts of the page are static and which will be replaced during transitions.

- `data-barba="wrapper"`: An outer wrapper that contains all page content. Elements outside the `container` but inside the `wrapper` will persist between page loads.
- `data-barba="container"`: The main content area that will be replaced with the new page's content.
- `data-barba-namespace`: A unique name for the page, used for defining transition rules.

```html
<body data-barba="wrapper">
    <header>
        <!-- Static header -->
    </header>
    <main data-barba="container" data-barba-namespace="home">
        <h1>Home Page</h1>
        <a href="/about.html">Go to About</a>
    </main>
    <footer>
        <!-- Static footer -->
    </footer>
</body>
```

### 2. Basic Transition

Transitions define the animations that occur when navigating between pages. You need an animation library like GSAP or Anime.js to handle the actual animations. This example uses CSS for a simple fade transition.

First, define the CSS:
```css
.fade-leave-active,
.fade-enter-active {
  transition: opacity 0.5s;
}
.fade-leave-to,
.fade-enter-from {
  opacity: 0;
}
```

Then, define the transition in your JavaScript:
```javascript
import barba from '@barba/core';
import { restart } from 'animejs';

barba.init({
  transitions: [{
    name: 'default-fade',
    leave(data) {
      // Animate the leaving page
      return new Promise(resolve => {
        data.current.container.classList.add('fade-leave-active', 'fade-leave-to');
        setTimeout(resolve, 500); // Match CSS transition duration
      });
    },
    enter(data) {
      // Animate the entering page
      data.next.container.classList.add('fade-enter-active');
      // Force a reflow to ensure the animation runs
      data.next.container.offsetHeight;
      data.next.container.classList.remove('fade-enter-from');
    }
  }]
});
```
*Note: In a real-world scenario, using an animation library like GSAP is recommended for more control, especially for handling the `done()` callback.*

## Directory Structure

This repository is a Lerna monorepo. The core logic and plugins are organized into separate packages:

- **`packages/core/`**: The main Barba.js engine that handles the PJAX navigation and transition lifecycle.
- **`packages/css/`**: A plugin to automatically add CSS classes to the `<html>` element during transitions, simplifying CSS-based animations.
- **`packages/prefetch/`**: A plugin that prefetches the content of pages when a user hovers over a link.
- **`packages/router/`**: A plugin that allows you to define transition rules based on page routes (e.g., `/user/:id`).
- **`documentation/`**: Contains the source for the official Barba.js documentation website.