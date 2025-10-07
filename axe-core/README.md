# axe-core

## Project Overview

`axe-core` is a lightweight, fast, and secure accessibility engine for automated web UI testing. It is designed to run in any modern browser and can be integrated into existing testing environments to identify accessibility defects during development.

## Core Features

- **Automated Testing**: Runs a comprehensive set of accessibility tests based on WCAG and other standards.
- **Framework Agnostic**: Works with any JavaScript framework.
- **Highly Configurable**: Allows for configuring rules, standards, and result formats.
- **No False Positives**: Designed to only return issues that it can accurately detect.
- **Cross-Domain Support**: Can test content within iframes across different domains.
- **Extensible**: Supports custom rules and checks through a plugin system.

## Installation & Setup

You can install `axe-core` via npm or include it directly from a CDN.

**NPM:**
```bash
npm install axe-core
```
Then, import it into your testing environment:
```javascript
import axe from 'axe-core';
```

**CDN:**
```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.4.1/axe.min.js"></script>
```

## Key Concepts & Usage

The primary function is `axe.run()`, which analyzes the page and returns a results object.

### Example 1: Basic Accessibility Scan

This example runs `axe.run` on the entire document and logs any violations to the console.

```javascript
// In the browser console or a script tag

axe.run(document, (err, results) => {
  if (err) {
    throw err;
  }
  if (results.violations.length > 0) {
    console.log('Accessibility Violations:');
    console.log(results.violations);
  } else {
    console.log('No accessibility violations found.');
  }
});
```
This will produce a `results` object containing `violations`, `passes`, `incomplete`, and `inapplicable` arrays.

### Example 2: Scanning a Specific Element with Options

This example demonstrates how to run `axe` on a specific part of the page (e.g., a modal) and configure the rules to only check for WCAG 2.0 Level AA compliance.

```javascript
const myElement = document.getElementById('my-modal');

const options = {
  runOnly: {
    type: 'tag',
    values: ['wcag2aa']
  }
};

axe.run(myElement, options, (err, results) => {
  if (err) throw err;
  console.log('WCAG 2 AA Violations:', results.violations);
});
```

## Directory Structure

- **`lib/`**: Contains the core source code for the accessibility engine, including rules and checks.
- **`doc/`**: Extensive documentation, including API guides, developer guides, and rule descriptions.
- **`build/`**: Scripts and tools used for building the distributable files.
- **`dist/`**: (This directory is not in the source but is created on build) Contains the compiled `axe.js` and `axe.min.js` files for distribution.
- **`test/`**: A comprehensive suite of unit and integration tests.
- **`locales/`**: Translation files for internationalization (i18n) of rule messages.