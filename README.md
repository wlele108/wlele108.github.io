# Henry Wang Personal Website — Maintenance Manual

This repository is a static bilingual personal website. The live page is the top-level `index.html`; its CSS and JavaScript are embedded in the same file. There is no build step, package manager, framework, `styles.css`, or `app.js`.

Use this file as the practical answer to: “Six months from now, what does every important file do, and where do I change something?”

## 1. Quick Start and Source of Truth

1. Open `index.html` directly in a browser for a quick review.
2. For reliable local testing, serve this folder with a simple static HTTP server and open the local URL.
3. Treat the current user request as the highest-priority instruction.
4. Use the latest résumé PDF as the source of truth for employers, titles, dates, locations, and accomplishments.
5. Keep every visible English `.en` field paired with a Chinese `.zh` field. The language switch works by adding and removing `.hidden`.

The main site does not use the Python files, notebooks, or `qixi-card/` to generate `index.html`. Editing or running those files will not update this website.

## 2. Site Structure

### Active site files and folders

| File / Folder | Purpose | Edit when... | Usually do not touch when... |
|---|---|---|---|
| `index.html` | Main one-page website. Contains Home, Interests, Experience & Education, Projects & Research, Contact, all site CSS, `PROJECT_DATA`, and all site JavaScript. | Changing visible site copy, links, project data, section content, styling variables, or interaction settings. | Updating only an image or PDF without changing its filename. |
| `README.md` | This maintenance manual. | Site structure, selectors, asset paths, or workflows change. | Making a small content correction that does not change the editing workflow. |
| `img/` | Local website images, including the hero, project thumbnails, and Interests media. | Adding or replacing site imagery. | Changing text or links. |
| `pdf/` | Résumé/CV downloads and older document files. | Replacing a downloadable CV or updating its filename. | Changing webpage content that does not affect downloads. |
| `gallery.html` | Current standalone Photography entry opened by the Photography item in Interests. This page is temporary: its imagery, content, information architecture, and visual treatment are scheduled for a complete future rebuild. | Beginning the dedicated Photography-page redesign or temporarily maintaining the current link target. | Changing only the homepage Photography slideshow; do not treat the current gallery content as final. |

### Reference, archive, and unrelated files

| File / Folder | Purpose | Edit when... | Usually do not touch when... |
|---|---|---|---|
| `gallery_calm_luxe.html` | Alternative/archived gallery visual experiment; not linked by the main page. | Intentionally developing that alternate gallery. | Maintaining the current `gallery.html`. |
| `gallery_editorial_calm.html` | Alternative/archived gallery visual experiment; not linked by the main page. | Intentionally developing that alternate gallery. | Maintaining the current `gallery.html`. |
| `index_old.html` | Legacy snapshot of an older homepage. It is not the main page. | Comparing historical implementation details. | Making current production changes. |
| `trial.html` | Legacy visual experiment; not referenced by `index.html`. | Explicitly revisiting that experiment. | Maintaining the current site. |
| `trial_1.html` | Legacy visual experiment; not referenced by `index.html`. | Explicitly revisiting that experiment. | Maintaining the current site. |
| `CODEX_PHASE_2_PROMPT.md` | Archived Phase 2 implementation brief. | Reviewing design history. | Applying a newer user request. |
| `CODEX_PHASE_2_1_PROMPT.md` | Archived Phase 2.1 implementation brief. | Reviewing design history. | Applying a newer user request. |
| `CODEX_PHASE_2_2_PROMPT.md` | Archived Phase 2.2 implementation brief. | Reviewing design history. | Applying a newer user request. |
| `qixi-card/` | Separate card project with its own assets, templates, Python generator, notebook, previews, and README. It does not generate the personal website. | Working specifically on the Qixi card project. | Updating `index.html`, Interests, Research, or the gallery. |
| `roulette.py` | Standalone roulette simulation/experiment. | Working on that simulation. | Updating the website. |
| `roulette_strategy_simulator (1).ipynb` | Standalone roulette notebook. | Working on that notebook. | Updating the website. |
| `roulette_strategy_simulator (2).ipynb` | Standalone roulette notebook. | Working on that notebook. | Updating the website. |
| `sketch.py` | Standalone experimental Python file. | Working explicitly on that experiment. | Updating the website. |
| `.DS_Store` and `img/.DS_Store` | macOS Finder metadata. | Never intentionally. | All website work. |

## 3. `index.html` Map

`index.html` is intentionally self-contained. Search for these stable IDs, selectors, and constants instead of relying on line numbers, which change over time.

| Target | Search for | What lives there |
|---|---|---|
| Global style variables | `:root` and `Phase 3: cinematic` | Colors, typography, hero image, cyan label sizes, slideshow timing. |
| Navigation | `id="navbar"` | Desktop menu, mobile menu, language buttons. |
| Home | `id="home"` | Hero name, Hero Identity, the embedded About Me introduction, CV and social links, editorial section links. |
| Archived About content | `id="about-content-archive"` | Inactive `<template>` retained for reference; it does not render as a page section. |
| Experience & Education | `id="experience"` | Bank of America first, other professional experience, and education. |
| Projects & Research | `id="projects"` | Empty `#projects-grid` mount point. Cards are rendered from `PROJECT_DATA`. |
| Interests | `id="interests"` | Photography slideshow, Skiing, Tennis, Basketball, Cooking. |
| Contact | `id="contact"` | Contact details, email copy controls, external links. |
| Project data | `const PROJECT_DATA` | The only content source for all nine default and detail project states. |
| Interaction settings | `const SITE_INTERACTION_CONFIG` | Slideshow interval, future video playback speed, and project pin flag. |

### Embedded CSS

There is no separate `styles.css`. The `<head>` contains Tailwind configuration and several embedded style blocks. The later rules intentionally override earlier historical rules, so add narrowly scoped fixes near the end of the final style block instead of broadly rewriting earlier layers.

Important variables:

| Variable | Current role |
|---|---|
| `--hero-image` | Home hero background. Currently points to `img/hero-ocean.jpg`. |
| `--cyan` | Restrained cyan accent used for labels and rules. |
| `--cyan-label-size-en` | English cyan-label size. |
| `--cyan-label-size-zh` | Chinese cyan-label size; intentionally optically larger. |
| `SITE_INTERACTION_CONFIG.PHOTOGRAPHY_SLIDE_INTERVAL` | Single JavaScript source of truth for the Photography hover slideshow interval; currently `1000`. |
| `#home::before` / `#home::after` rgba alpha | Hero overlay strength and text contrast. |

Research images must remain `object-fit: contain`, centered on a neutral charcoal frame. Do not switch them to `cover`; the full source image is more important than filling every pixel.

### Embedded JavaScript

There is no separate `app.js`. The scripts in `index.html` handle:

- desktop and mobile language switching;
- mobile-menu opening and closing;
- smooth anchor scrolling;
- navbar scroll state;
- email copying and icon feedback;
- rendering all Research cards from `PROJECT_DATA`;
- Research hover/focus detail visibility;
- experimental click-to-pin behavior;
- Photography hover slideshow;
- Photography previous/next controls;
- future Skiing/Tennis video preview behavior.

`SITE_INTERACTION_CONFIG.ENABLE_PROJECT_PIN` controls the experimental pin feature:

- `true`: clicking a project pins the same detail state used by hover; clicking it again unpins; pinning another project closes the previous one.
- `false`: click-to-pin listeners are not installed; normal hover/focus and mobile static details still work.

The comment `EXPERIMENTAL — PROJECT PIN` must remain next to this behavior until the feature is accepted permanently.

## 4. Asset Guide

### `img/`

| Path | Contents and use |
|---|---|
| `img/hero-ocean.jpg` | Current Home hero photograph, referenced by `--hero-image`. |
| `img/trade.jpg` | Derivative-Trading Simulation Fund thumbnail. |
| `img/reg.jpg` | Real Estate Financial Model thumbnail. |
| `img/ghana.jpg` | Ghana Economic Research thumbnail. |
| `img/epayment.jpg` | E-Payment Economic Impact thumbnail. |
| `img/af.jpg` | Camera autofocus project thumbnail. |
| `img/stata.jpg` | Work-From-Home project thumbnail. |
| `img/figma3.jpg` | USC Transportation Heatmap thumbnail. |
| `img/figma.jpg` | Sickle Cell Anaemia app thumbnail. |
| `img/fossil.jpg` | Assistant Tutoring project thumbnail. |
| `img/interests/photography/` | Categorized homepage Photography slideshow assets under `nature-landscape/`, `city-architecture/`, and `night-atmosphere/`. The explicit HTML order controls playback order. |
| `img/interests/tennis/tennis-court-poster.jpg` | Current static Tennis poster and future video fallback image. |
| Other root-level images | Existing education, portrait, legacy, or supporting assets. Confirm references with a text search before deleting or renaming any file. |

Do not assume an image is unused merely because it is not part of `PROJECT_DATA`; Experience, archived About content, or legacy pages may still reference it.

### `pdf/`

The Home CV buttons currently reference:

- English: `pdf/Resume.pdf`
- Chinese: `pdf/王乐桓中文简历.pdf`

To update a CV safely, either replace the existing PDF while keeping its filename, or update the matching Home `href`. Then open both language versions and confirm the correct file loads.

`pdf/Resume.docx`, `pdf/王乐桓中文简历.docx`, `pdf/Jessie_Lyu_Resume.pdf`, and the remaining documents are not linked by the current Home CV controls. Do not replace them as part of a normal Henry website update unless explicitly requested.

## 5. Editing Homepage Copy

In `index.html`, search inside `#home` for these selectors:

- Hero Identity English: `<p class="hero-identity en">`
- Hero Identity Chinese: `<p class="hero-identity zh hidden">`
- About Me visible label: `.hero-about-label` (`About Me` / `关于我`)
- About Me paragraph English: the `<p class="en">` inside `.hero-about`
- About Me paragraph Chinese: the `<p class="zh hidden">` inside `.hero-about`

Edit English and Chinese together. Keep the existing element hierarchy so the language switch and layout continue to work. The casual tone is intentional; do not automatically turn the introduction into résumé or cover-letter language.

The visible `About Me` label and the paragraph beneath it are separate fields. A label-only request must not rewrite the paragraph. This remains an embedded Home component; do not recreate a standalone About section.

### Homepage module labels

The four `.hero-index` modules use the same primary names as the persistent menu: `Interests`, `Experience`, `Research`, and `Contact`. The matching bilingual primary names live in `.hero-index-title`; the smaller explanatory phrases live separately in `.hero-index-description`. Keep the primary titles synchronized with the menu whenever navigation labels change.

To update the hero background, add the photograph under `img/`, then change `--hero-image`. Adjust only the overlay alpha values if the new photograph needs more or less contrast.

### Experience & Education maintenance

- Desktop: `#experience .grid.md\:grid-cols-2` uses two equal `1fr` columns, approximately 50% Experience and 50% Education.
- Desktop divider: `#experience .grid.md\:grid-cols-2::after` draws the subtle centered vertical dashed rule. It is inside a `min-width: 768px` media query, so it does not appear on mobile.
- Mobile: the existing narrow-layout rule changes the grid to one column, stacking Experience above Education without a vertical divider.
- Booth location fields: `Chicago` / `芝加哥`.
- USC location fields: `Los Angeles` / `洛杉矶`.
- Location fields use `.education-location`; update the English and Chinese values together and do not globally replace city names.

## 6. Adding or Editing a Project

All project content now lives once in `const PROJECT_DATA` near the bottom of `index.html`. The default card and hover/pinned detail view are rendered from that same object.

Each project record contains:

```text
id
image
title.en / title.zh
shortDescription.en / shortDescription.zh
tags.en[] / tags.zh[]
detailTitle.en / detailTitle.zh
details.en[] / details.zh[]
```

Workflow:

1. Add the project image to `img/` using a descriptive filename.
2. Add a new object to `PROJECT_DATA`, or edit the existing object.
3. Provide paired English and Chinese titles.
4. Provide paired English and Chinese short descriptions.
5. Provide English and Chinese tags in the same order and with the same array length.
6. Provide paired detail titles and detailed bullet arrays.
7. Keep each English and Chinese bullet array factually equivalent.
8. Verify the default card shows image, title, short description, and tags.
9. Verify hover and keyboard focus show non-empty details.
10. Switch EN/中文 and verify both default and detail content change.
11. Verify click, second-click unpin, and one-pinned-at-a-time behavior when `ENABLE_PROJECT_PIN` is `true`.
12. Verify desktop hover does not change card dimensions and mobile details remain directly accessible.

Default content and hover content are different levels of detail, but they must belong to the same project data source. Do not paste a second copy of project content into `#projects-grid`; that element must remain an empty rendering mount point.

To change project order, move the complete object within `PROJECT_DATA`. To change a thumbnail, update only that object’s `image` field. Keep `object-fit: contain` in the Research CSS.

### Research detail overlay contract

The desktop Research interaction is intentionally an in-frame replacement, not a text panel below the image:

- `.project-card` is the fixed visual frame and remains the same size before, during, and after hover.
- `.project-detail` must remain a child of that card and use `position: absolute`, `inset: 0`, `width: 100%`, and `height: 100%` so it covers the existing image/title outline inside the exact same border.
- The detail layer uses `overflow-y: auto` and `overflow-x: hidden`. Long `<li>` content scrolls inside the project box; it must never expand the grid row or appear below the card.
- Hidden detail layers use `pointer-events: none`. A visible `.is-detail-preview` or `.is-detail-open` layer uses `pointer-events: auto`, which is required for trackpad, mouse-wheel, and scrollbar access.
- Keep the card wrapper `position: relative` and `overflow: hidden` so the overlay cannot escape its border.
- On coarse-pointer and narrow mobile layouts, the detail layer returns to normal relative flow and remains directly visible. Do not require hover on touch devices.
- Project cards are generated after Tailwind's browser-side class scan. Do not rely only on generated utility classes such as `absolute` and `inset-0` for critical overlay positioning; preserve the explicit, narrowly scoped `#projects ... > .project-detail` CSS fallback near the end of the final style block.

When this interaction is edited, inspect one long-detail card as well as all nine cards. Confirm that the detail layer's bounding box matches the card, `scrollHeight` may exceed `clientHeight`, internal scrolling changes the detail layer's `scrollTop`, and the surrounding grid does not move.

## 7. Interests Media Guide

### Photography

- Add new slideshow photographs to the most appropriate category folder, not directly to the Photography root.
- Every compatible image should have one `.photography-frame` `<img>` inside `[data-photography-slideshow]` in `#interests`. A static `file://` page cannot enumerate folders, so filenames and playback order remain explicit in the HTML.
- The first HTML frame is the resting image and must carry `.is-active`. The current default is `img/interests/photography/night-atmosphere/starry-sky-01.jpeg`.
- Slideshow timing has one source of truth: `SITE_INTERACTION_CONFIG.PHOTOGRAPHY_SLIDE_INTERVAL` in the embedded JavaScript. Its value is `1000`, so the resting frame and every later frame each receive one full second after hover begins.
- Hover starts one interval; mouse leave clears it and preserves the currently displayed frame. Manual previous/next selection restarts the same interval so the newly selected frame also gets a full second.
- To reorder the slideshow later, move the complete `.photography-frame` elements within `[data-photography-slideshow]`; do not duplicate paths in JavaScript.
- If fewer images appear than expected, compare the explicit `src` list with the category folders. The slideshow skips missing, unfinished, or failed images (`complete === false` or `naturalWidth === 0`) instead of displaying a broken frame.
- Previous/next buttons use `[data-photography-direction]`. They appear only while the Photography item is hovered and remain siblings of `.interest-primary-link`, preventing a manual step from opening `gallery.html`.
- Images use `object-fit: contain` and must not be compressed, stretched, cropped, or dimensionally altered without explicit approval.
- The whole Photography item links to `gallery.html`. The homepage slideshow and future gallery remain separate image lists; `gallery.html` is still a temporary destination scheduled for a later rebuild.

### Photography folder structure

```text
img/interests/photography/
├── nature-landscape/
├── city-architecture/
└── night-atmosphere/
```

- `nature-landscape/`: coastlines, weather, mountains, open roads, the lighthouse, and other outdoor subjects led by the natural environment.
- `city-architecture/`: urban streets, interiors, transit, and built-environment studies.
- `night-atmosphere/`: the star field, night city scenes, dusk silhouettes, sunsets, reflections, and mood-led low-light work.

### Nature & Landscape

- `balloon-moon-01.jpeg`
- `coastal-lighthouse-01.jpeg`
- `ocean-sunset-birds-01.jpeg`
- `coastal-cliff-01.jpeg`
- `snowy-mountain-road-01.jpeg`
- `mountain-lake-dusk-01.jpeg`
- `rainbow-bridge-01.jpeg`

### City & Architecture

- `station-clock-01.jpeg`
- `city-street-01.jpeg`
- `grand-staircase-01.jpeg`
- `hillside-train-01.jpeg`

### Night & Atmosphere

- `starry-sky-01.jpeg` — default/resting slideshow image
- `harbor-skyline-night-01.jpeg`
- `bridge-sunset-01.jpeg`
- `bridge-sunset-02.jpeg`
- `city-sunset-01.jpeg`
- `reflected-sunset-01.jpeg`
- `waterfront-dusk-01.jpeg`
- `beach-photographer-dusk-01.jpeg`

### Skiing

- Skiing is currently an editorial text card with no image, poster, or video path.
- If a Skiing video is supplied later, create `img/interests/skiing/`, store the video and optional poster there, add a muted looping `<video>` inside a media wrapper, and add `data-video-interest="skiing"` to the card.
- Playback speed comes from `SITE_INTERACTION_CONFIG.INTEREST_VIDEO_PLAYBACK_RATE`.

### Tennis

- Current poster: `img/interests/tennis/tennis-court-poster.jpg`.
- Future video: place it beside the poster, then replace the image in `.interest-media` with a muted, looping, `playsinline` `<video>` using the poster as fallback.
- Keep `data-video-interest="tennis"`; existing JavaScript will play on hover for compatible devices and use `INTEREST_VIDEO_PLAYBACK_RATE`.
- There is no Tennis video in the repository yet; do not rename the poster to a video extension.

### Basketball

- Basketball currently uses the compact editorial supporting-card treatment and has no image.
- To add one later, create `img/interests/basketball/`, add a contained media layer inside the existing Basketball article, and preserve its bilingual title and description.

### Cooking

- Cooking currently uses the compact editorial supporting-card treatment and has no image.
- To add one later, create `img/interests/cooking/`, add a contained media layer inside the existing Cooking article, and preserve its bilingual title and description.

## Photography Asset Migration Manifest

This manifest is the source of truth for mirroring the local migration in `wlele108/wlele108.github.io`. Every row is a lossless filesystem move/rename; no image pixels, dimensions, or quality were changed.

| Old path | New path | New filename | Category | Used where |
|---|---|---|---|---|
| `img/interests/photography/DSC_0637.jpeg` | `img/interests/photography/night-atmosphere/starry-sky-01.jpeg` | `starry-sky-01.jpeg` | Night & Atmosphere | Homepage Photography slideshow — first/default |
| `img/interests/photography/DSC_0063.jpeg` | `img/interests/photography/night-atmosphere/harbor-skyline-night-01.jpeg` | `harbor-skyline-night-01.jpeg` | Night & Atmosphere | Homepage Photography slideshow |
| `img/interests/photography/DSC_3834.jpeg` | `img/interests/photography/night-atmosphere/bridge-sunset-01.jpeg` | `bridge-sunset-01.jpeg` | Night & Atmosphere | Homepage Photography slideshow |
| `img/interests/photography/DSC_3837.jpeg` | `img/interests/photography/night-atmosphere/bridge-sunset-02.jpeg` | `bridge-sunset-02.jpeg` | Night & Atmosphere | Homepage Photography slideshow |
| `img/interests/photography/DSC_3853.jpeg` | `img/interests/photography/night-atmosphere/city-sunset-01.jpeg` | `city-sunset-01.jpeg` | Night & Atmosphere | Homepage Photography slideshow |
| `img/interests/photography/DSC_3908.jpeg` | `img/interests/photography/night-atmosphere/reflected-sunset-01.jpeg` | `reflected-sunset-01.jpeg` | Night & Atmosphere | Homepage Photography slideshow |
| `img/interests/photography/IMG_1325.jpeg` | `img/interests/photography/night-atmosphere/waterfront-dusk-01.jpeg` | `waterfront-dusk-01.jpeg` | Night & Atmosphere | Homepage Photography slideshow |
| `img/interests/photography/d3d4a6efc3df486c49779e9cfdf887f2.jpeg` | `img/interests/photography/night-atmosphere/beach-photographer-dusk-01.jpeg` | `beach-photographer-dusk-01.jpeg` | Night & Atmosphere | Homepage Photography slideshow |
| `img/interests/photography/DSC_1734.jpeg` | `img/interests/photography/nature-landscape/balloon-moon-01.jpeg` | `balloon-moon-01.jpeg` | Nature & Landscape | Homepage Photography slideshow |
| `img/interests/photography/DSC_2078.jpeg` | `img/interests/photography/nature-landscape/coastal-lighthouse-01.jpeg` | `coastal-lighthouse-01.jpeg` | Nature & Landscape | Homepage Photography slideshow |
| `img/interests/photography/DSC_2125.jpeg` | `img/interests/photography/nature-landscape/ocean-sunset-birds-01.jpeg` | `ocean-sunset-birds-01.jpeg` | Nature & Landscape | Homepage Photography slideshow |
| `img/interests/photography/DSC_2516.jpeg` | `img/interests/photography/nature-landscape/coastal-cliff-01.jpeg` | `coastal-cliff-01.jpeg` | Nature & Landscape | Homepage Photography slideshow |
| `img/interests/photography/DSC_3025.jpeg` | `img/interests/photography/nature-landscape/snowy-mountain-road-01.jpeg` | `snowy-mountain-road-01.jpeg` | Nature & Landscape | Homepage Photography slideshow |
| `img/interests/photography/DSC_4161.jpeg` | `img/interests/photography/nature-landscape/mountain-lake-dusk-01.jpeg` | `mountain-lake-dusk-01.jpeg` | Nature & Landscape | Homepage Photography slideshow |
| `img/interests/photography/IMG_1359.jpeg` | `img/interests/photography/nature-landscape/rainbow-bridge-01.jpeg` | `rainbow-bridge-01.jpeg` | Nature & Landscape | Homepage Photography slideshow |
| `img/interests/photography/DSC_0087.jpeg` | `img/interests/photography/city-architecture/station-clock-01.jpeg` | `station-clock-01.jpeg` | City & Architecture | Homepage Photography slideshow |
| `img/interests/photography/DSC_0105.jpeg` | `img/interests/photography/city-architecture/city-street-01.jpeg` | `city-street-01.jpeg` | City & Architecture | Homepage Photography slideshow |
| `img/interests/photography/DSC_1532.jpeg` | `img/interests/photography/city-architecture/grand-staircase-01.jpeg` | `grand-staircase-01.jpeg` | City & Architecture | Homepage Photography slideshow |
| `img/interests/photography/Z30_0368.jpeg` | `img/interests/photography/city-architecture/hillside-train-01.jpeg` | `hillside-train-01.jpeg` | City & Architecture | Homepage Photography slideshow |

## 8. Editing Links and Contact Information

- CV links: search for `pdf/Resume.pdf` and `pdf/王乐桓中文简历.pdf`.
- LinkedIn: search for `linkedin.com/in/henry-wang`.
- Instagram: search for `instagram.com/wlele__`.
- Email, phone, and location: search the exact visible value and update all matching Home, Contact, and Footer occurrences.
- Photography destination: search for `href="gallery.html"`.

After changing any link, test it from the rendered page. Keep `target="_blank"` behavior where it already exists.

## 9. Validation Checklist

Before considering a website edit complete:

- [ ] Home renders at desktop and mobile widths.
- [ ] Mobile menu opens and its anchors work.
- [ ] EN/中文 switch changes all paired content without mixing languages.
- [ ] Home shows `About Me` / `关于我`, while the introduction paragraph remains unchanged.
- [ ] Home module primary titles match the persistent menu in both languages.
- [ ] Bank of America remains the first professional Experience entry.
- [ ] Booth shows Chicago / 芝加哥 and USC shows Los Angeles / 洛杉矶.
- [ ] Experience and Education are equal-width on desktop with one subtle centered dashed divider; mobile stacks without the vertical divider.
- [ ] Both CV links, LinkedIn, Instagram, Photography, and contact links open the intended target.
- [ ] Email copy still works.
- [ ] No horizontal overflow appears at mobile width.
- [ ] Browser console contains no new errors.
- [ ] All local images and PDFs return successfully.
- [ ] Reduced-motion and coarse-pointer users can still access Research detail content.
- [ ] Desktop Research details cover the original card in the same frame and long bullet lists scroll inside that frame.
- [ ] Photography hover reveals both translucent controls; previous/next changes only the image, and automatic hover playback advances every one second.
- [ ] All 19 Photography files resolve from the three category folders, and `starry-sky-01.jpeg` is first/default.

For each of the nine Research cards:

- [ ] image visible and undistorted;
- [ ] default title visible;
- [ ] default short description visible;
- [ ] default tags visible;
- [ ] hover/focus detail content is not empty;
- [ ] correct detail bullets appear;
- [ ] mouse leave restores the outline unless pinned;
- [ ] EN/中文 changes both default and detail content;
- [ ] click pins when enabled;
- [ ] second click unpins;
- [ ] only one card is pinned at a time;
- [ ] hover does not change card dimensions.

## 10. Current TODO

### Copy

- [ ] Revisit Hero Identity if desired
- [ ] Revisit the About Me paragraph if desired

### Media

- [ ] Final homepage background
- [ ] Final Photography slideshow selection
- [ ] Final Skiing video
- [ ] Final Tennis video
- [ ] Optional Basketball image
- [ ] Optional Cooking image

### Projects

- [ ] Review project thumbnails
- [ ] Review short descriptions
- [ ] Review detailed bullets
- [ ] Decide whether to keep `ENABLE_PROJECT_PIN`

### Visual

- [ ] Final cyan-label size
- [ ] Final Chinese typography scale
- [ ] Photography slideshow speed
- [ ] Video preview speed
- [ ] Hero overlay strength

## Updating the Live GitHub Website

The live repository is `wlele108/wlele108.github.io`. Local editing and review happen first. Synchronize to GitHub only after the local version has been verified; do not use GitHub as the first place to test path migrations.

### A. Before uploading

From the local checkout of `wlele108.github.io`, verify the intended versions of:

- `index.html`;
- `README.md`;
- every changed, renamed, or moved image;
- PDFs, only when a PDF was intentionally changed;
- all local paths, with no broken image or document reference.

### B. Photography folder changes require special care

A Photography rename or folder migration requires GitHub to receive both:

1. every new file at its new category path;
2. deletion of every obsolete old path.

Uploading only the new folders leaves duplicate assets in the repository. Use the `Photography Asset Migration Manifest` above as the source of truth for the exact old-to-new mapping.

### C. Recommended Git workflow

Run the following only after copying the locally verified changes into the local checkout of `wlele108.github.io`:

```bash
git status
git add -A
git status
git commit -m "Describe the website update"
git push
```

- First `git status`: inspect the unstaged local changes.
- `git add -A`: stage new files, modified files, deleted old files, and detected moves/renames. This is essential after Photography folder migrations.
- Second `git status`: inspect the exact staged result before committing.
- `git commit`: create the local repository revision with a specific message.
- `git push`: send the verified commit to `wlele108/wlele108.github.io`.

### D. Verify what Git thinks changed

Before committing, read the second `git status`. A Photography migration may appear as:

```text
renamed: old/path/image.jpeg -> new/path/image.jpeg
```

or as separate entries:

```text
deleted: old/path/image.jpeg
new file: new/path/image.jpeg
```

Both representations can be normal; Git's similarity-based rename detection determines which one appears. The important requirement is that the new path is staged and the old path is staged for deletion.

### E. Large photo warning

- Do not place RAW camera files in the GitHub Pages repository.
- Use web-exported JPEG or WebP files for the live website and keep RAW originals outside the repository.
- GitHub normally hard-blocks individual Git objects above 100 MiB, and large assets below that limit can still make the page slow.
- Do not automatically compress existing photographs; prepare and review any web derivative deliberately.

### F. Final GitHub verification

After pushing, verify:

- the repository contains `nature-landscape/`, `city-architecture/`, and `night-atmosphere/` under `img/interests/photography/`;
- all 19 obsolete root-level Photography paths are removed;
- all 19 new categorized files exist;
- `index.html` paths match GitHub filename capitalization exactly;
- GitHub Pages loads without broken images;
- `night-atmosphere/starry-sky-01.jpeg` is the default image;
- hover playback and manual arrows work at the live URL.

## Next GitHub Sync

- [ ] Upload/update `index.html`.
- [ ] Upload/update `README.md`.
- [ ] Create `img/interests/photography/nature-landscape/` in the GitHub checkout.
- [ ] Create `img/interests/photography/city-architecture/` in the GitHub checkout.
- [ ] Create `img/interests/photography/night-atmosphere/` in the GitHub checkout.
- [ ] Add all 19 renamed Photography files listed in the migration manifest.
- [ ] Remove all 19 obsolete root-level Photography paths listed in the migration manifest.
- [ ] Confirm `img/interests/photography/night-atmosphere/starry-sky-01.jpeg` exists and is the first `.photography-frame`.
- [ ] Verify every `index.html` Photography path against the case-sensitive GitHub filenames.
- [ ] Verify the migration manifest against the staged GitHub changes.
- [ ] Confirm no PDF change is included in this revision.
- [ ] Run `git status` before staging.
- [ ] Stage the migration with `git add -A`.
- [ ] Run `git status` again before committing.
- [ ] Commit with a descriptive message.
- [ ] Push to `wlele108/wlele108.github.io`.
- [ ] Verify GitHub Pages, the starry-sky resting image, one-second slideshow timing, and manual arrows.
