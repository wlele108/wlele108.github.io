# Henry Wang Personal Website — Maintenance Manual

This is the source of truth for the current local bilingual portfolio. The site is static: there is no framework, package manager, bundler, or server-side production runtime. The approved visual system is dark, cinematic, restrained, and editorial.

The source/development version documented here is:

`/Users/henry/Desktop/Daily Use/Resume/2025/personal website/demo/`

This directory is **not** currently a Git repository. The separate local GitHub checkout is expected to be named `wlele108.github.io`; verify its real path before copying or staging anything.

## 1. Information Architecture

The permanent top-level navigation is:

1. Home
2. Work
3. Interests
4. Contact

Header and footer navigation must always use these four items in this order.

`Work` contains Experience, Education, and Research. `Interests` contains Photography, Cooking, Tennis, Basketball, and Skiing.

The active pages are:

- `index.html` — Home, Work, Interests, Contact, and the existing Research section.
- `gallery.html` — Photography detail page beneath Interests.
- `kitchen.html` — Cooking detail page beneath Interests.

Gallery and Kitchen are child pages, not top-level navigation entries. On both child pages, Home, Work, Interests, and Contact point back to the corresponding `index.html` anchors.

## 2. Active File and Folder Map

| Path | Runtime role | Maintenance rule |
|---|---|---|
| `index.html` | Main portfolio, including the curated homepage Photography slideshow and Kitchen preview. | Preserve Work, Research, About, Contact, and current interactions unless a task explicitly targets them. |
| `gallery.html` | Production Photography archive, orientation filters, balanced rows, and lightbox. | This is the public Gallery target; layout reads only from centralized photo metadata. |
| `gallery2.html` | Read-only experimental Gallery archive. | Superseded layout experiments only; do not edit, publish, or use as the Photography link target. |
| `kitchen.html` | Data-driven bilingual Kitchen Notes archive. | Recipe content reads only from the recipe dataset. |
| `css/subpage-shell.css` | Shared Gallery/Kitchen navigation, type, spacing, and footer shell. | Keep both child pages visually coherent. |
| `data/photo-metadata.js` | One metadata record per Gallery photograph. | Human-maintained location/style/comment fields and EXIF-derived fields live here. |
| `data/recipes.js` | All 50 recipe records. | Chinese content follows the private source document; English remains a faithful companion. |
| `scripts/build_photo_metadata.py` | Optional EXIF refresh utility. | Maintenance-only; the live website never requires Python. |
| `img/interests/photography/` | Flat storage for all 43 Photography images. | All images live directly in this directory. No style subfolders. Keep `new/` as an empty staging folder between imports. |
| `img/interests/tennis/tennis-court-poster.jpg` | Current Tennis media. | Unchanged by the Photography system. |
| `img/*.jpg` | Research and supporting images. | Preserve active filenames and `PROJECT_DATA` paths. |
| `pdf/Resume.pdf` | English CV. | Replace only when explicitly supplied. |
| `pdf/王乐桓中文简历.pdf` | Chinese CV. | Replace only when explicitly supplied. |
| `菜谱.docx` | Private local recipe source of truth. | Not a public runtime asset; do not modify or publish without authorization. |
| `README.md` | Architecture, maintenance, validation, and deployment handoff. | Update with every structural or data-system revision. |

`gallery2.html`, other archived Gallery variants, old/trial HTML, `qixi-card/`, roulette files, notebooks, and unrelated experiments do not generate the active pages.

`gallery2.html` specifically preserves superseded justified-row, fixed 4:5 frame, square-frame, and alternative fit-strategy tests. Future maintenance must not copy its accumulated override layers back into production. `gallery.html` is the Gallery source of truth.

## 3. Navigation, Language, and Content Boundaries

When a top-level label or anchor changes, update the desktop header, mobile menu, footer, child-page shells, and Home modules together. All new visible copy needs paired `.en` and `.zh` content. Language preference is shared through `localStorage` key `henry-site-language`.

The Interests section uses natural labels:

1. Photography / 摄影
2. Cooking / 烹饪
3. Tennis / 网球
4. Basketball / 篮球
5. Skiing / 滑雪

Photography and Cooking receive larger, content-rich layouts; their hierarchy comes from composition and scale rather than a mechanical hierarchy label. Tennis, Basketball, and Skiing remain restrained supporting entries.

The Kitchen preview count is generated from `window.RECIPES.length` and appears as natural editorial copy such as `50 recipes`, never as a hard-coded KPI.

Do not change Experience, Education, Research, `PROJECT_DATA`, Research hover/pin behavior, About Me, or Contact while maintaining Photography. The exact approved About sentence remains:

> I study at Chicago Booth and will be returning to BofA in S&T.

## 4. Homepage Photography Contract

The homepage slideshow is maintained separately from the Gallery dataset. A new Gallery photograph must be added to `index.html` explicitly when the user requests homepage inclusion.

Current behavior:

- `starry-sky-01.jpeg` is the initial, resting, and first frame.
- `SITE_INTERACTION_CONFIG.PHOTOGRAPHY_SLIDE_INTERVAL = 2000` is the only autoplay timing source.
- The fade is approximately 220 ms.
- Desktop/fine pointer: hover starts playback; leave stops and restores the starry frame; arrows affect the slideshow only.
- Touch/coarse pointer: 44 px arrows remain visible, horizontal swipe works, and `IntersectionObserver` starts autoplay at about 50% visibility.
- Leaving the viewport pauses playback and restores the starry frame.
- Manual arrow/swipe input resets the same interval; overlapping intervals are not allowed.
- Reduced-motion disables autoplay and collapses transitions while preserving manual controls.
- Only the explicit Gallery CTA navigates to `gallery.html`.

All homepage slideshow paths use the flat Photography directory. The photographs imported on 2026-08-27 were added after the resting starry frame in newest-to-oldest order; the six photographs from the 2026-08-26 revision remain intentionally excluded. The homepage sequence now contains 37 frames, including `IMG_1737.jpeg`.

## 5. Production Gallery: Balanced Rows, Filters, and Lightbox Filmstrip

The Gallery is intentionally a dense, image-first photo album rather than a sparse exhibition page. Its visible bilingual page title is `摄影集`, and the space beneath the hero is shortened so photography begins sooner.

The visible Gallery quote is user-provided content, not independently authenticated:

> “A photograph is time held still. When we grow old enough to forget how to remember, it will still remember our youth for us.”
>
> — Ansel Adams

> “照片是凝固的时间，等我们老到忘了如何回忆，它依然替我们年轻着”
>
> — 安塞尔·亚当斯  
> 摄影界的“约塞米蒂诗人”

Edit the wording and attribution only in the `.gallery-quote` block in `gallery.html`. Treat it as user-authored/provided copy.

### Balanced overview rows

The production overview is one continuous newest-to-oldest sequence. It has no physical year or month groups and no large year dividers. `renderGallery()` removes the pinned records from the later chronology. All and Landscape retain the approved three-photo balanced rows; Portrait alone uses four equal-width photographs per desktop row so vertical images remain shorter. Final rows remain left-aligned and may contain fewer photographs.

Every photograph receives a compact capture label immediately above it (`AUG 2025` in English or `2025年8月` in Chinese). Repeated month/year labels are intentional because the date belongs to the photograph rather than a physical group.

The balancing algorithm uses actual `aspectRatio` metadata, with natural image dimensions as a runtime fallback. It softens extreme ratios with `ratio ** ROW_BALANCE_POWER`, then bounds each full-row share before generating the row's CSS grid columns. Photographs remain in chronological order; they are never reordered for visual convenience.

The exact production configuration is:

```js
GALLERY_CONFIG = {
  SORT_DIRECTION: "newest-first",
  PHOTOS_PER_ROW: 3,
  PORTRAIT_PHOTOS_PER_ROW: 4,
  ORIENTATION_SPLIT: 1,
  ROW_BALANCE_POWER: 0.6,
  MIN_CELL_SHARE: 0.24,
  MAX_CELL_SHARE: 0.42
}
```

Desktop/tablet gutters are `6px`; narrow-mobile gutters are `4px`. Portrait remains four-across responsively, while All and Landscape remain three-across. Overview images use `width: 100%; height: auto` and never use `object-fit: cover`, so they are not cropped, stretched, or compressed into fixed frames.

### Thumbnail location behavior

Normal thumbnails permanently show only the compact capture-month label. Location, comment, style, and EXIF are not permanently visible. `photoMarkup()` places the metadata-driven `.image-location` inside `.gallery-image-button`. On fine-pointer desktop, `.gallery-image-button:hover .image-location` fades in a small bottom-left location tag; keyboard `:focus-visible` receives the same cue. The image change is limited to a very slight brightness/scale adjustment.

Under `@media (hover: none), (pointer: coarse)` and the narrow-mobile breakpoint, `.image-location` stays hidden, so mobile never depends on hover or accumulates a returned-focus label after closing the lightbox. A single tap continues to open the lightbox. Full location, date, optional comment, and EXIF remain in `renderLightbox()`.

### Pinned opening photographs

The understated opening selection is rendered by `#gallery-pinned` and `#gallery-pinned-grid` before the chronological archive. It is configured only through `pinnedOrder` in `data/photo-metadata.js`:

1. `starry-sky-01.jpeg` — Joshua Tree National Park, CA — `pinnedOrder: 1`
2. `balloon-moon-01.jpeg` — Mexico City — `pinnedOrder: 2`
3. `coastal-cliff-01.jpeg` — Oregon Coast, OR — `pinnedOrder: 3`

`renderGallery()` sorts positive `pinnedOrder` values and omits those records from the later archive, so no image file or rendered thumbnail is duplicated. The pinned selection uses the same softened, bounded row-width logic as chronology. Under All, all three remain pinned. Under an orientation filter, only pinned photographs with the matching derived orientation appear; an empty pinned group is hidden.

To pin or unpin a photograph later, change only its metadata field: use a unique positive integer for its order or `pinnedOrder: null` to return it to chronology. Do not modify `gallery.html`.

### Chronology, orientation, and capture-device filters

Gallery ordering is controlled by one value:

```js
GALLERY_CONFIG.SORT_DIRECTION = "newest-first"
```

The visible filters are `All / Landscape / Portrait` and `全部 / 横幅 / 竖幅`. Orientation is derived automatically: `aspectRatio < ORIENTATION_SPLIT` is portrait and `aspectRatio >= ORIENTATION_SPLIT` is landscape. `styleTags` remain intact in metadata for future use but do not drive the production filter controls.

A second, checkbox-based row filters by capture device. `Camera / 相机` is checked by default and `Phone / 手机` is unchecked, so the initial view shows the 36 dedicated-camera photographs. Camera includes both Nikon bodies as well as the Fujifilm and Panasonic records; the seven iPhone records are classified as Phone from their EXIF `camera` value. The device checkboxes combine with the orientation buttons, and users may select either, both, or neither without changing chronology or lightbox behavior.

Filtering preserves the same newest-to-oldest sequence before it is chunked into rows. The All lightbox sequence contains 43 unique photographs. The overview renders the three pinned photographs once and the other 40 once; the lightbox filmstrip uses the complete filtered unique sequence.

### Lightbox filmstrip

The approved main-image and information layout remains unchanged. `#lightbox-filmstrip` is a single horizontal, no-wrap, touch-scrollable strip rendered by `renderFilmstrip()` from the exact same `filteredPhotos()` sequence used by the counter and previous/next controls.

- Each thumbnail directly selects its photograph without closing the lightbox.
- `renderLightbox()` synchronizes the main image, bilingual location, date, optional comment, EXIF, counter, and the single `.is-active` thumbnail.
- Every lightbox view includes a visible `Comments / 备注` section. Its text remains empty until `comment.en` and `comment.zh` are populated in metadata.
- Previous/next buttons, Arrow Left/Arrow Right, and thumbnail clicks all use the same `lightboxIndex`.
- `centerActiveThumbnail()` scrolls only the filmstrip to center the active thumbnail; reduced-motion uses immediate scrolling and other users receive restrained smooth scrolling.
- Thumbnail height is `56px` on desktop and approximately `45px` on mobile. Filmstrip buttons use each photograph's real aspect ratio and `object-fit: contain`, so horizontal and vertical thumbnails remain fully visible.
- The scrollbar is visually hidden, while horizontal wheel/touch scrolling and keyboard-focusable thumbnail buttons remain available.

## 6. Flat Photography Storage

All Photography files live directly in:

`img/interests/photography/`

**STYLE TAG ≠ FILESYSTEM LOCATION.** Style classification lives only in `styleTags`. Never move an image merely to change a Gallery filter.

### Complete 2026-08-26 migration manifest

| Old path | New path |
|---|---|
| `img/interests/photography/city-architecture/city-street-01.jpeg` | `img/interests/photography/city-street-01.jpeg` |
| `img/interests/photography/city-architecture/grand-staircase-01.jpeg` | `img/interests/photography/grand-staircase-01.jpeg` |
| `img/interests/photography/city-architecture/hillside-train-01.jpeg` | `img/interests/photography/hillside-train-01.jpeg` |
| `img/interests/photography/city-architecture/station-clock-01.jpeg` | `img/interests/photography/station-clock-01.jpeg` |
| `img/interests/photography/nature-landscape/balloon-moon-01.jpeg` | `img/interests/photography/balloon-moon-01.jpeg` |
| `img/interests/photography/nature-landscape/coastal-cliff-01.jpeg` | `img/interests/photography/coastal-cliff-01.jpeg` |
| `img/interests/photography/nature-landscape/coastal-lighthouse-01.jpeg` | `img/interests/photography/coastal-lighthouse-01.jpeg` |
| `img/interests/photography/nature-landscape/mountain-lake-dusk-01.jpeg` | `img/interests/photography/mountain-lake-dusk-01.jpeg` |
| `img/interests/photography/nature-landscape/ocean-sunset-birds-01.jpeg` | `img/interests/photography/ocean-sunset-birds-01.jpeg` |
| `img/interests/photography/nature-landscape/rainbow-bridge-01.jpeg` | `img/interests/photography/rainbow-bridge-01.jpeg` |
| `img/interests/photography/nature-landscape/snowy-mountain-road-01.jpeg` | `img/interests/photography/snowy-mountain-road-01.jpeg` |
| `img/interests/photography/night-atmosphere/beach-photographer-dusk-01.jpeg` | `img/interests/photography/beach-photographer-dusk-01.jpeg` |
| `img/interests/photography/night-atmosphere/bridge-sunset-01.jpeg` | `img/interests/photography/bridge-sunset-01.jpeg` |
| `img/interests/photography/night-atmosphere/bridge-sunset-02.jpeg` | `img/interests/photography/bridge-sunset-02.jpeg` |
| `img/interests/photography/night-atmosphere/city-sunset-01.jpeg` | `img/interests/photography/city-sunset-01.jpeg` |
| `img/interests/photography/night-atmosphere/harbor-skyline-night-01.jpeg` | `img/interests/photography/harbor-skyline-night-01.jpeg` |
| `img/interests/photography/night-atmosphere/reflected-sunset-01.jpeg` | `img/interests/photography/reflected-sunset-01.jpeg` |
| `img/interests/photography/night-atmosphere/starry-sky-01.jpeg` | `img/interests/photography/starry-sky-01.jpeg` |
| `img/interests/photography/night-atmosphere/waterfront-dusk-01.jpeg` | `img/interests/photography/waterfront-dusk-01.jpeg` |

The obsolete `nature-landscape/`, `city-architecture/`, and `night-atmosphere/` directories are removed only after their files are moved and verified.

### Newly supplied Photography files

These files were already present in the development folder and are now registered in Gallery metadata:

- `img/interests/photography/DSC_0571.jpg`
- `img/interests/photography/DSC_0709.jpg`
- `img/interests/photography/DSC_1624.jpeg`
- `img/interests/photography/DSC_2585 7F7E53F3.jpg`
- `img/interests/photography/DSC_4175.jpg`
- `img/interests/photography/Z30_0224.jpg`

There is no separate `DSC_2585.*` and no separate `7F7E53F3.*`. The actual filesystem contains one photograph named `DSC_2585 7F7E53F3.jpg`; it therefore receives one metadata record and is not duplicated or renamed.

### 2026-08-27 `new/` import

Seventeen images were moved without renaming from `img/interests/photography/new/` into the flat Photography root and registered in Gallery metadata and the homepage slideshow:

- `DSC_0326.jpeg`, `DSC_1098.jpeg`, `DSC_1101.jpeg`, `DSC_1105.jpeg`, `DSC_1118.jpeg`
- `DSC_1691.jpeg`, `DSC_1701.jpeg`, `DSC_2734.jpeg`, `DSC_3238.jpeg`, `DSC_3286.jpeg`
- `IMG_0615.jpeg`, `IMG_0618.jpeg`, `IMG_0979.jpeg`, `IMG_1157.jpeg`, `IMG_1269.jpeg`, `IMG_7815.jpeg`, `IMG_7818.jpeg`

The library increased from 25 to 42 actual images and metadata records. Keep `img/interests/photography/new/` present but empty as the staging location for the next import. For each future batch: inspect exact filenames, check for root collisions, extract EXIF, move the files into the flat root, rebuild metadata, add user-supplied bilingual locations, decide homepage inclusion, verify counts, and leave `new/` empty.

A later same-day follow-up replaced the existing bytes for `IMG_0615.jpeg`, `IMG_1157.jpeg`, and `IMG_1269.jpeg`, and added `IMG_1737.jpeg` (`Upstate New York / 纽约州北部`). The final library contains 43 images/records; the homepage slideshow contains 37 frames.

## 7. Central Photo Metadata Schema

`gallery.html` renders only from `window.PHOTO_METADATA` in `data/photo-metadata.js`. Each actual image has exactly one record:

```js
{
  file: "starry-sky-01.jpeg",
  src: "img/interests/photography/starry-sky-01.jpeg",
  dateTaken: "2025-01-20T11:09:12",
  year: 2025,
  month: 1,
  location: {
    en: "Joshua Tree National Park, CA",
    zh: "约书亚树国家公园，CA"
  },
  locationStatus: "confirmed",
  locationNote: "",
  styleTags: ["night-atmosphere"],
  styleStatus: "classified",
  pinnedOrder: 1,
  aspectRatio: 1.5,
  camera: "NIKON Z 7_2",
  lens: "NIKKOR Z 24-200mm f/4-6.3 VR",
  focalLength: "30 mm",
  aperture: "f/4.5",
  shutter: "13 s",
  iso: "6400",
  comment: { en: "", zh: "" },
  exifSource: "DateTimeOriginal",
  rawCaptureTime: "2025:01:20 11:09:12"
}
```

Human-maintained fields:

- `location.en`, `location.zh`
- `locationStatus`, `locationNote`
- `styleTags`, `styleStatus`
- `comment.en`, `comment.zh`
- `pinnedOrder`

EXIF/machine-derived fields:

- `dateTaken`, `year`, `month`, `exifSource`, `rawCaptureTime`
- `camera`, `lens`, `focalLength`, `aperture`, `shutter`, `iso`, `aspectRatio`

Capture-time precedence is `DateTimeOriginal`, then `DateTimeDigitized`, then embedded image `DateTime`. Finder Created, Modified, and Last Opened timestamps are never photographic dates.

The maintenance script scans only the flat Photography root, refreshes machine-derived fields, and preserves human fields by exact filename. It preserves `pinnedOrder`, normalizes unpinned records to `null`, and stops rather than silently processing nested style folders, duplicate filenames, or duplicate positive pin positions.

## 8. Location Display Convention

Visible locations use the concise `city/location, state/region` scale and do not append country names. US states use abbreviations such as `CA`, `OR`, `IL`, and `NV`; Hong Kong uses `HK`. Examples include `Joshua Tree National Park, CA`, `Chicago, IL`, `Deep Water Bay, HK`, `Yangpu Bridge, Shanghai`, and `Mexico City`.

Do not display `Near ...` or `...附近`. When the exact place is intentionally unknown, use `Somewhere, [region]` / `某处，[region]`; if no reliable region is known, use `Somewhere` / `某处`. Locations remain human-maintained metadata and must not be inferred from adjacent filenames.

Point Vicente, Dockweiler State Beach, East Coast Park Precinct, and all 2026-08-27 import locations are user-provided or previously confirmed. The new files remain `styleTags: []` and `styleStatus: "unclassified"` until the user assigns styles manually.

## 9. Photo Maintenance Workflows

### Update a style

Edit only `styleTags` and `styleStatus` in `data/photo-metadata.js`:

```js
styleTags: ["city-architecture"],
styleStatus: "classified"
```

No file move, image rename, or `gallery.html` edit is required.

### Update a location

Edit only `location.en`, `location.zh`, `locationStatus`, and `locationNote`. Do not edit Gallery layout code.

### Add a comment

Edit `comment.en` and `comment.zh`. Blank comments render no placeholder. Populated comments appear in the lightbox between date and camera information.

### Pin or unpin a Gallery photograph

Edit only `pinnedOrder` in `data/photo-metadata.js`:

```js
pinnedOrder: 1 // positive, unique order in the opening selection
pinnedOrder: null // unpinned; render in chronological archive
```

The Gallery reads this value dynamically. No image move, duplicate file, or `gallery.html` edit is required.

### Add a new photograph

1. Export a web-ready image while preserving EXIF.
2. Place it in `img/interests/photography/new/`, preserving its real filename and extension.
3. Inspect the complete staging batch and verify that no filename collides with the flat root.
4. Extract EXIF, move each imported image into `img/interests/photography/`, and leave `new/` present but empty.
5. Run `python3 scripts/build_photo_metadata.py` from the development project root.
6. Verify the capture timestamp and camera fields, then enter the bilingual location and status manually.
7. Optionally maintain `styleTags`, comments, and a unique positive `pinnedOrder`; leave unpinned records `null`.
8. Add requested images to the homepage slideshow explicitly; the Gallery dataset does not inject them automatically.
9. Verify newest-first Gallery ordering, All/Landscape three-across rows, Portrait four-across rows, pinned behavior, lightbox, homepage sequence, and mobile layout.
10. Later mirror the documented image and code changes into the verified Git checkout.

## 10. Kitchen Notes

`kitchen.html` renders 50 recipes from `data/recipes.js`. Chinese source content comes from private `菜谱.docx`; English is a faithful companion. Recipe categories, vegetarian metadata, search, accordions, and future Wine/Cocktail collection architecture remain unchanged.

The Kitchen page shows `50 recipes` when unfiltered and a natural `n of 50 recipes` result when filtering/searching. Counts come from the dataset.

`window.RECIPE_COLLECTIONS` continues to reserve independent future collections:

```js
{ recipes: true, wine: false, cocktails: false }
```

Wine remains a future tasting/menu archive, not a food category. Cocktails remain a separate future drinks collection. No content may be invented.

## 11. Validation Rules

Before deployment, verify:

- all actual image files have one metadata record and vice versa;
- homepage and Gallery use only flat Photography paths;
- chronological ordering remains newest-first without year/month physical groups;
- every full All/Landscape overview row contains three photographs and every full Portrait row contains four; only final rows may contain fewer;
- the balanced row shares use actual aspect ratios, the documented power, and the documented 24%–42% bounds without reordering;
- the dense Gallery uses 6 px/4 px gutters, natural aspect ratios, and a compact date label above every photograph; Portrait remains visibly shorter at four-across;
- All/Landscape/Portrait filtering derives orientation from aspect ratio while preserving chronology;
- Camera/Phone checkboxes derive capture type from EXIF camera names, default to Camera only (36), combine with orientation filters, and show all 43 photographs when both are checked;
- unclassified style records remain available because visible filtering no longer depends on `styleTags`;
- normal thumbnails contain no permanently visible location, comment, style, or EXIF metadata;
- fine-pointer hover/focus reveals only the correct location tag, while coarse-pointer/mobile keeps that location hidden and shows only the compact date label;
- the pinned opening contains exactly starry sky, balloon moon, and coastal cliff in metadata-driven order, without later thumbnail duplication;
- full locations and dates render in the lightbox, whose filtered filmstrip stays synchronized with direct thumbnail, button, and keyboard navigation;
- the active filmstrip thumbnail centers within the strip without scrolling the page, and reduced-motion disables smooth centering;
- blank comments render nothing;
- starry-sky remains the homepage default;
- desktop hover, mobile arrows/swipe, 2000 ms autoplay, and 220 ms fade remain intact;
- EN/中文, mobile menus, Header/Footer, Gallery/Kitchen CTAs, Research, Contact, links, PDFs, and local assets still work;
- there is no horizontal overflow or revision-caused console error.

## 12. Revision Log

### 2026-08-26 — Chronological Photography Metadata, Locations & Flat Storage

- Removed the former mechanical hierarchy wording from visible Interests labels.
- Naturalized the dynamic Kitchen count.
- Softened the Gallery `Moments & Places` display scale.
- Replaced the technical Gallery intro with the user-provided Ansel Adams wording.
- Implemented newest-to-oldest year/month rendering with one heading per group.
- Removed repeated thumbnail dates and made location the thumbnail label.
- Flattened Photography storage without changing filenames, bytes, pixels, dimensions, compression, quality, or EXIF.
- Converted the three former physical categories into metadata-only style tags.
- Centralized 25 records with bilingual location/status/style/comment fields and EXIF fields.
- Confirmed the user-provided Point Vicente, Dockweiler State Beach, and East Coast Park Precinct locations.
- Processed six actual newly supplied files; no nonexistent separate DSC/7F file was fabricated.
- Left all six newly supplied images style-unclassified.
- Made Gallery photo count derive from the filtered metadata dataset.
- Kept homepage slideshow selection separate and preserved its prior 19-frame sequence.
- Prepared the deployment migration manifest and deletion list; no Git command was run.
- Changed Gallery spacing from a loose exhibition layout to dense photo-album masonry with small gutters and natural image ratios.
- Hid thumbnail metadata by default and moved the location to a subtle fine-pointer hover/focus label; full metadata remains in the lightbox.
- Added the metadata-driven pinned opening: Joshua Tree star field, Mexico City balloon, then Oregon Coast.
- Retained year/month chronology while compacting its headings and inter-group spacing.
- Corrected the three bridge photographs to Yangpu Bridge, Shanghai / 上海杨浦大桥.
- Preserved the flat storage and centralized metadata architecture; no image storage migration occurred in this Gallery refinement.

## Revision — 2026-08-26: Production Gallery Balanced Rows + Lightbox Filmstrip

- Confirmed `gallery.html` as the production Photography page; retained `gallery2.html` unchanged as a read-only archive of superseded experiments.
- Replaced public style filters with bilingual All/Landscape/Portrait controls derived from each photograph's aspect ratio.
- Removed year/month physical grouping and rendered one continuous newest-first sequence in three-photo rows.
- Added a compact English/Chinese month-year label above every photograph, including the pinned selection.
- Implemented softened aspect-ratio weights (`ratio ** 0.6`) with 24% minimum and 42% maximum full-row shares, without cropping, stretching, or visual reordering.
- Consolidated the production overview into one balanced-row CSS/JavaScript system instead of retaining conflicting frame or fit overrides.
- Preserved starry sky, balloon moon, and coastal cliff as the metadata-driven pinned opening and omitted those records from later chronology.
- Retained the approved lightbox main-image and information layout, then added a synchronized horizontal filmstrip with direct navigation, active state, counter/keyboard/previous-next parity, active-thumbnail centering, touch scrolling, and reduced-motion handling.
- Kept all 25 image files, all metadata content, and the Yangpu Bridge bilingual location records unchanged.
- Modified only the production `gallery.html` and this `README.md`; no Git command was run.

## Revision — 2026-08-27: Photo Import, Locations & Portrait Density

- Imported 17 photographs from `new/` into flat storage, increasing the library from 25 to 42 files/records; all EXIF fields used by the site were readable.
- Added all 17 imported photographs to the homepage slideshow while preserving starry sky as the resting first frame.
- Normalized visible bilingual locations to concise place/region labels without country names or `Near / 附近`; vague locations use `Somewhere / 某处`.
- Changed Portrait only to four equal-width photographs per row; All and Landscape remain three-photo balanced rows and every overview image retains its full natural ratio.
- Renamed the visible pinned heading to `Pinned / 置顶` without changing the three pinned records or their order.
- Renamed the Gallery hero title to `摄影集`, added a visible empty `Comments / 备注` area to every lightbox view, replaced three supplied image files, and added `IMG_1737.jpeg` from Upstate New York.
- Kept `img/interests/photography/new/` present and empty for the next batch.

## Revision — 2026-08-27: Capture-device Filter

- Added bilingual `Camera / 相机` and `Phone / 手机` checkboxes directly below the orientation controls.
- Defaulted the Gallery to dedicated-camera photographs while keeping phone photographs available with one click.
- Classified the current EXIF-backed collection as 36 camera photographs and seven phone photographs; both Nikon bodies, Fujifilm, and Panasonic remain in Camera.
- Combined capture-device selection with the existing All/Landscape/Portrait filters, pinned selection, count, overview, and lightbox sequence.
- Modified only production `gallery.html` and this `README.md` for this revision.

## Next GitHub Sync — Deployment Handoff

### Current 2026-08-27 sync delta

Files modified:

- `index.html` — adds the imported photographs, including `IMG_1737.jpeg`, to the homepage Photography sequence.
- `gallery.html` — Portrait four-across logic, `Pinned / 置顶`, `摄影集`, and the empty lightbox Comments area.
- `data/photo-metadata.js` — 43 EXIF-backed records and normalized bilingual locations.
- `README.md` — inventory, workflow, conventions, validation, and this handoff.

Files moved from `img/interests/photography/new/` to `img/interests/photography/` without renaming:

- `DSC_0326.jpeg`, `DSC_1098.jpeg`, `DSC_1101.jpeg`, `DSC_1105.jpeg`, `DSC_1118.jpeg`
- `DSC_1691.jpeg`, `DSC_1701.jpeg`, `DSC_2734.jpeg`, `DSC_3238.jpeg`, `DSC_3286.jpeg`
- `IMG_0615.jpeg`, `IMG_0618.jpeg`, `IMG_0979.jpeg`, `IMG_1157.jpeg`, `IMG_1269.jpeg`, `IMG_7815.jpeg`, `IMG_7818.jpeg`

Follow-up image delta: replace `IMG_0615.jpeg`, `IMG_1157.jpeg`, and `IMG_1269.jpeg`; add `IMG_1737.jpeg`.

Follow-up capture-filter delta: sync only `gallery.html` and `README.md`; no photo or metadata files changed.

Deployment counts: **43 actual Photography images / 43 metadata records**. The empty `img/interests/photography/new/` staging directory should remain local; Git does not track empty directories unless a placeholder is deliberately added. Verify the separate Git checkout before any eventual sync. Do not publish `.DS_Store` or unrelated/private files.

The remainder of this section records the superseded 2026-08-26 deployment handoff for history.

The **source/development version** is:

`/Users/henry/Desktop/Daily Use/Resume/2025/personal website/demo/`

The intended **GitHub local checkout** is a separate directory named `wlele108.github.io`. Its actual path and existing status must be verified before copying or staging. Do not assume the development directory is the Git checkout.

### A. Files modified

- `gallery.html`
- `README.md`

These are the only files changed in the Production Gallery Balanced Rows + Lightbox Filmstrip revision. The larger historical deployment inventory below remains for the earlier flat-storage migration, but it is not a claim that those files changed again in this revision.

Additional 2026-08-26 production Gallery balanced-row sync delta:

- `gallery.html`: production orientation filters, continuous balanced three-photo rows, per-photo date labels, and the synchronized lightbox filmstrip.
- `README.md`: production/reference file distinction, exact balance configuration, filter/filmstrip behavior, validation, and this handoff.
- `gallery2.html`: unchanged, read-only experimental archive; it is not a deployment target and remains outside the public Photography link.
- `data/photo-metadata.js`, all image files, and all other site files: unchanged by this revision.
- This revision created no files, moved no files, renamed nothing, changed no metadata content, and ran no Git command.

### B. Files created

- None

### C. Files moved / renamed

Use the complete 19-row old-path/new-path table in [Section 6](#complete-2026-08-26-migration-manifest). No filename or extension changed; each file moved from a style subdirectory directly into `img/interests/photography/`.

### D. Files/directories that must be deleted from GitHub

The old paths in the migration table must disappear from the remote checkout. After their tracked files move, these obsolete directories must no longer exist:

- `img/interests/photography/city-architecture/`
- `img/interests/photography/nature-landscape/`
- `img/interests/photography/night-atmosphere/`

### E. New Photography files

- `img/interests/photography/DSC_0571.jpg`
- `img/interests/photography/DSC_0709.jpg`
- `img/interests/photography/DSC_1624.jpeg`
- `img/interests/photography/DSC_2585 7F7E53F3.jpg`
- `img/interests/photography/DSC_4175.jpg`
- `img/interests/photography/Z30_0224.jpg`

Requested-basename audit:

- `DSC_0571`: found
- `DSC_0709`: found
- `DSC_1624`: found
- `DSC_2585`: no separate basename; appears only inside `DSC_2585 7F7E53F3.jpg`
- `7F7E53F3`: no separate basename; appears only inside `DSC_2585 7F7E53F3.jpg`
- `DSC_4175`: found
- `Z30_0224`: found

The combined DSC/7F filename is one file and one photograph, not two.

Final deployment counts:

- Actual Photography files: **25**
- Metadata records: **25**
- Counts match: **Yes**

### F. Files intentionally NOT changed

- CV PDFs and other PDFs are unchanged.
- Research project content and assets are unchanged.
- Experience, Education, About, Contact, and `PROJECT_DATA` are unchanged.
- `data/recipes.js` and the private `菜谱.docx` recipe source are unchanged.
- `css/subpage-shell.css` is unchanged.
- No photo was renamed, duplicated, recompressed, resized, or edited.
- Archived/trial HTML, notebooks, `qixi-card/`, and unrelated scripts are unchanged.

### Local verification completed

- [x] `index.html` opens
- [x] `gallery.html` opens
- [x] `kitchen.html` opens
- [x] Home navigation works
- [x] Gallery CTA works
- [x] Kitchen CTA works
- [x] Header/footer navigation is consistent
- [x] EN / 中文 works
- [x] Photography homepage slideshow works
- [x] Desktop hover playback works
- [x] Mobile/touch arrows work
- [ ] Mobile swipe works
- [x] Slideshow still uses 2000 ms interval
- [x] Starry-sky image remains the default
- [x] Gallery sorts newest → oldest
- [x] Gallery renders one continuous sequence without year/month physical groups
- [x] Compact month/year labels appear above every photograph
- [x] Every full chronology row contains three photographs; only the final row may contain fewer
- [x] Dense Gallery gutters are 6 px desktop/tablet and 4 px narrow mobile
- [x] Natural thumbnail aspect ratios are preserved without crop or stretch
- [x] Desktop location labels reveal on hover and hide on leave
- [x] Mobile thumbnails keep locations hidden before and after lightbox use; only compact date labels remain visible
- [x] Pinned order is starry sky, balloon moon, coastal cliff; none repeat in chronology
- [x] All/Landscape/Portrait filters work, including filter-aware pinned photographs
- [x] Orientation derives from aspect ratio rather than `styleTags`
- [x] Unclassified style records remain visible under the orientation filters
- [x] Lightbox works
- [x] Filmstrip order, active thumbnail, counter, direct selection, previous/next, and keyboard navigation remain synchronized
- [x] Filmstrip touch scrolling and active-thumbnail centering remain isolated to the strip
- [x] Reduced-motion uses immediate filmstrip centering
- [x] EXIF metadata renders where available
- [x] Blank comments do not render placeholder UI
- [x] Yangpu Bridge renders correctly in English and Chinese
- [x] No broken image paths
- [x] No horizontal overflow at tested desktop and mobile widths
- [x] No browser-console errors caused by this revision

The desktop in-app browser cannot emit a native `TouchEvent`, so the existing swipe listener could not be conclusively exercised on actual touch hardware. Its code path and threshold were preserved; verify this one unchecked item on a physical phone before deployment.

Because this migration contains modifications, additions, deletions, and file moves, the future verified Git checkout should eventually use `git add -A`. That command stages modifications, additions, deletions, and detected moves/renames together. **Do not run it in the development folder and do not run it before ChatGPT has inspected the real `wlele108.github.io` checkout.** No staging, commit, or push was performed in this revision.

## What to Send ChatGPT for Deployment

Return to ChatGPT with:

1. this updated `README.md`;
2. the final Codex completion summary;
3. preferably the output of `git status` from the local `wlele108.github.io` checkout **before** copying or staging anything;
4. the actual local path to that checkout, plus the development path above if either location changes.

ChatGPT can then compare the exact migration manifest against the real checkout and provide safe copy/staging/commit/push commands without guessing.
