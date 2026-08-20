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
| Home | `id="home"` | Hero name, Hero Identity, Short Introduction, CV and social links, editorial section links. |
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
| `--photography-slideshow-interval` | Photography hover slideshow interval in milliseconds. |
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
| `img/interests/photography/` | Local source images available to the homepage Photography hover slideshow. Because a static page cannot enumerate the folder, only filenames explicitly listed in `index.html` are shown. |
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
- Short Introduction English: the `<p class="en">` inside `.hero-about`
- Short Introduction Chinese: the `<p class="zh hidden">` inside `.hero-about`

Edit English and Chinese together. Keep the existing element hierarchy so the language switch and layout continue to work. The casual tone is intentional; do not automatically turn the introduction into résumé or cover-letter language.

To update the hero background, add the photograph under `img/`, then change `--hero-image`. Adjust only the overlay alpha values if the new photograph needs more or less contrast.

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

- Upload slideshow images to `img/interests/photography/`.
- Every compatible image currently in this folder should have one `.photography-frame` `<img>` inside `[data-photography-slideshow]` in `#interests`; no filename or category is displayed on the page.
- The current homepage list contains all 19 non-system JPEG images present in the folder.
- The first frame should also carry `.is-active`.
- Keep the HTML list synchronized when files are added or removed. A page opened with `file://` cannot securely enumerate a local folder by itself, so the filenames must remain explicitly referenced in `index.html`.
- If the slideshow appears to contain fewer images than expected, compare the explicit `src` list with the folder first. The slideshow deliberately skips missing, unfinished, or failed images (`complete === false` or `naturalWidth === 0`) instead of displaying a broken frame.
- Change speed through `--photography-slideshow-interval`; the current value is `1000ms` (one second per image).
- The previous/next buttons use `[data-photography-direction]`. They appear only while the Photography item is hovered and use restrained transparency. Clicking a button changes the active frame without opening `gallery.html` and restarts the one-second hover cycle from that frame.
- Keep the controls as siblings of `.interest-primary-link`, not nested inside the gallery link. This preserves valid interactive HTML and prevents a manual image step from opening a new page.
- Images use `object-fit: contain` and should not be compressed, stretched, or destructively cropped without explicit approval.
- The whole Photography item links to the active `gallery.html`. The slideshow and gallery are separate image lists.
- `gallery.html` is only the current placeholder destination. Henry plans to rebuild that page and replace all of its present content later; future homepage work should preserve the link without treating the current gallery structure as a design constraint.

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
- [ ] Bank of America remains the first professional Experience entry.
- [ ] Both CV links, LinkedIn, Instagram, Photography, and contact links open the intended target.
- [ ] Email copy still works.
- [ ] No horizontal overflow appears at mobile width.
- [ ] Browser console contains no new errors.
- [ ] All local images and PDFs return successfully.
- [ ] Reduced-motion and coarse-pointer users can still access Research detail content.
- [ ] Desktop Research details cover the original card in the same frame and long bullet lists scroll inside that frame.
- [ ] Photography hover reveals both translucent controls; previous/next changes only the image, and automatic hover playback advances every one second.

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
- [ ] Revisit A Short Introduction if desired

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

## 11. GitHub Upload and GitHub Pages

The current `demo/` folder is not yet a Git repository. Its active website is already suitable for static hosting because `index.html` is at the project root and there is no build step.

### Before the first upload

1. Decide whether the GitHub repository will be public or private. A public GitHub Pages site necessarily makes the published HTML, referenced images, and downloadable CVs public.
2. Review the folder before staging. `qixi-card/`, roulette scripts/notebooks, legacy HTML experiments, old résumé documents, and macOS `.DS_Store` files do not run the main website. Do not publish private or unrelated material merely because it shares this folder.
3. Add a `.gitignore` before the first commit. At minimum it should contain:

   ```gitignore
   .DS_Store
   **/.DS_Store
   __pycache__/
   *.pyc
   ```

4. Check large assets before every first upload. The current folder is approximately 108 MB; its largest individual image is approximately 10 MB, so there is currently no file above GitHub's 25 MiB browser-upload limit. GitHub warns for files larger than 50 MiB and blocks files larger than 100 MiB. Do not replace or compress source photography without Henry's approval.
5. On GitHub, create a new empty repository. Do not pre-populate it with a README, license, or `.gitignore`, because this folder already contains the local starting point.

### First command-line upload

Run these commands in Terminal, replacing the two uppercase placeholders with the actual GitHub account and repository names:

```bash
cd "/Users/henry/Desktop/Daily Use/Resume/2025/personal website/demo"
git init -b main
git status
git add .
git status
git commit -m "Initial Henry Wang portfolio"
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Read the second `git status` before committing. It is the final check that no private or unrelated file is included. If GitHub asks for authentication, use the browser/device flow provided by Git Credential Manager or a personal access token; do not put a password or token in this repository.

### Publish with GitHub Pages

After the push completes:

1. Open the repository on GitHub.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select branch **main**, folder **/(root)**, then save.
5. Wait for the Pages deployment to finish. The expected address is `https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/` and the future gallery address is `https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/gallery.html`.

The site loads Tailwind and web fonts from external CDNs, so an internet connection is still required for the intended styling. GitHub Pages paths are case-sensitive; preserve asset filename capitalization.

### Later updates

After editing and validating the site:

```bash
cd "/Users/henry/Desktop/Daily Use/Resume/2025/personal website/demo"
git status
git add -A
git status
git commit -m "Update photography gallery"
git push
```

Use a commit message that describes the actual change. GitHub Pages will redeploy automatically after a successful push to `main`.

Official references:

- [Adding locally hosted code to GitHub](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github)
- [Configuring a publishing source for GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [About large files on GitHub](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github)
