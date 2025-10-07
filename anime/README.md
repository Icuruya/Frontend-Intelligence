# anime.js

## Project Overview

Anime.js is a lightweight and powerful JavaScript animation engine. It works with any CSS properties, SVG attributes, DOM attributes, and JavaScript Objects, making it a versatile tool for adding motion to web projects.

## Core Features

- **Multi-target animation**: Animate multiple targets at once.
- **Timeline control**: Create complex, synchronized animation sequences.
- **Playback controls**: Play, pause, restart, seek, and reverse animations.
- **Versatile targeting**: Works with CSS selectors, DOM elements, and JavaScript objects.
- **Extensive easing library**: Includes a wide range of easing functions, including spring physics.
- **SVG animation**: Excels at animating SVG attributes, including line drawing and morphing.

## Installation & Setup

You can install Anime.js via npm or include it directly from a CDN.

**NPM:**
```bash
npm install animejs
```
Then, import it into your project:
```javascript
import anime from 'animejs/lib/anime.es.js';
```

**CDN:**
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>
```

## Key Concepts & Usage

The core of Anime.js is the `anime()` function, which takes an object of animation parameters.

### Example 1: Basic Property Animation

This example moves a DOM element 250px to the right and rotates it 360 degrees.

```html
<div class="box"></div>
<script>
  anime({
    targets: '.box',
    translateX: 250,
    rotate: '1turn',
    backgroundColor: '#FFF',
    duration: 800
  });
</script>
```

### Example 2: Timeline Animation

Timelines allow for sequencing multiple animations. This example animates three boxes in sequence with a slight overlap.

```html
<div class="box red"></div>
<div class="box blue"></div>
<div class="box green"></div>
<script>
  var timeline = anime.timeline({
    easing: 'easeOutExpo',
    duration: 750
  });

  timeline
    .add({
      targets: '.red',
      translateX: 250
    })
    .add({
      targets: '.blue',
      translateX: 250
    }, '-=600') // Starts 600ms before the previous animation ends
    .add({
      targets: '.green',
      translateX: 250
    }, '-=600');
</script>
```

## Directory Structure

- **`src/`**: Contains the raw, uncompiled source code of the library.
- **`dist/`**: Contains the compiled and minified versions of the library, ready for production use.
- **`examples/`**: A directory with a wide variety of practical examples showcasing the library's features.
- **`tests/`**: Unit and integration tests for the library.