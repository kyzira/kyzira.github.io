# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Static website for **Friseursalon Team Hava**, a hair salon in Tuttlingen, Germany. Hosted on GitHub Pages with custom domain `friseursalon-team-hava.de`.

## Development

**No build system** - this is a static HTML/CSS/JavaScript site. Changes are deployed instantly when pushed to the main branch.

### Gallery Update Utility

To regenerate before/after gallery HTML from image files:
```bash
python update_gallery.py
```
This scans `assets/vorher/` and `assets/nachher/` directories and updates the gallery blocks in index.html.

## Architecture

Single-page application with three core files:
- **index.html** - All HTML structure plus inline JavaScript (~320 lines of JS at end of file)
- **styles.css** - Complete styling with CSS variables for theming
- **update_gallery.py** - Python utility for gallery generation

### Key JavaScript Features (inline)
- Intersection Observer for scroll reveal animations
- Mobile hamburger menu with overlay
- Lightbox gallery with touch swipe and keyboard navigation
- Leaflet.js map integration (OpenStreetMap)

### Styling Conventions
- Dark luxury theme with gold accents
- CSS variables: `--gold: #d4af37`, `--bg0: #000000`, `--text: #f5f5f5`
- Fonts: Cormorant Garamond (headings), Inter (body)
- Responsive breakpoints at 700px and 900px

### Third-Party Dependencies (CDN)
- Leaflet.js v1.9.4 for maps
- Google Fonts

### Assets Structure
- `assets/salon/` - Salon interior gallery images
- `assets/vorher/` and `assets/nachher/` - Before/after portfolio images
- `assets/*.png/jpg` - Logo, hero, team, service images, icons

## Language

All content is in German (de).
