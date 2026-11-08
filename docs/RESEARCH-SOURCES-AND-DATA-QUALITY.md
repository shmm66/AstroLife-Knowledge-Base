# Research sources and data quality — release 0.2.0

This document describes why each source family is included and what it can and cannot support. Accessed 2026-11-09.

## 1. Astronomy and numerical reference data

### NASA Jet Propulsion Laboratory — Horizons
URL: https://ssd.jpl.nasa.gov/horizons/manual.html

Use for time-specific ephemerides and calculation conventions. A reproducible request records target, epoch, time scale, observing centre, reference frame, coordinate type, corrections and relevant output settings. An ephemeris is not itself an astrological interpretation.

### NASA Jet Propulsion Laboratory — Planetary Physical Parameters
URL: https://ssd.jpl.nasa.gov/planets/phys_par.html

The structured reference file in `data/reference/planetary-parameters.json` records selected table fields for Mercury through Neptune and the five dwarf planets listed in the table. These include radii, mass, density, sidereal rotation and orbital periods, V(1,0), geometric albedo, equatorial gravity and escape velocity.

Important table definitions:
- Mean radius is the radius of a sphere with equivalent volume.
- Sidereal rotation period is the time for one rotation relative to fixed stars.
- Sidereal orbital period is the time for one orbit relative to fixed stars.
- V(1,0) is defined for a distance of 1 au from both Sun and observer; it is not apparent magnitude as seen from Earth.
- Negative rotation values for Venus, Uranus, Neptune and some dwarf planets indicate retrograde spin under the table's convention.

Uncertainties are copied only where the JPL table explicitly displays them. Missing uncertainty values mean “not supplied in this table”, not zero uncertainty. Values retain units and are not mixed with birth-time chart positions.

### International Astronomical Union — 2006 resolutions
URL: https://www.iau.org/IAU/Iau/News/PR2006/iau-2006-general-assembly-resolution-votes.aspx

Use for the IAU's Solar System planet/dwarf-planet definitions. The eight planets are Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune. Pluto is a dwarf planet; this astronomical classification is separate from whether a modern astrological school uses Pluto symbolically.

### IAU constellations
Use the IAU constellation boundary convention for modern astronomical mapping. Do not equate those bounded regions with twelve equal 30-degree zodiac signs.

## 2. Historical sources

### John Steele, Oxford reference on Babylonian astronomy (2021)
URL: https://academic.oup.com/edited-volume/61673/chapter-abstract/550534232

Used for a scholarly summary of Mesopotamian observation, mathematical astronomy and celestial divination. It documents historical practices and categories; it does not establish their predictive validity.

### Ptolemaeus Arabus et Latinus — Tetrabiblos
URL: https://ptolemaeus.badw.de/work/27

Used for scholarly catalogue and transmission history of the Tetrabiblos through Greek, Arabic and Latin traditions. The treatise is evidence of historical doctrine and its reception, not a modern experimental standard.

## 3. Empirical studies and methodological reviews

### Hartmann, Reuter & Nyborg (2006)
DOI: https://doi.org/10.1016/j.paid.2005.11.017

Examined birth-date zodiac groupings and individual differences in a large sample and reported no support for zodiac-based differences in personality or general intelligence. Do not generalise beyond the tested variables and study design.

### Kelly (1979)
DOI: https://doi.org/10.2466/pr0.1979.44.3c.1231

A review of empirical astrology research. It is included as a literature-history source; it should be read alongside later studies and methodological debate.

### Carlson (1985), Wyman & Vyse (2008), and Ertel (2010)
Carlson DOI: https://doi.org/10.1038/318419a0  
Wyman & Vyse: https://doi.org/10.3200/GENP.135.3.287-300  
Ertel DOI: https://doi.org/10.2466/PR0.101.3.929-939

These works examine particular natal-chart/personality-matching procedures. The repository summarises the tests and the subsequent methodological discussion without claiming that astrology was verified by the reanalysis or that one experiment settles every cultural or symbolic claim.

### Helgertz & Scott (2020)
URL: https://link.springer.com/article/10.1186/s41118-020-00103-5

Longitudinal analysis of Swedish register data for 1968–2001. The authors found no consistent evidence that astrologically more compatible couples were overrepresented among observed marriages or had lower divorce risk. The result concerns the specific pairings and Swedish records examined.

### Joshanloo (2024)
DOI: https://doi.org/10.1111/kykl.12395

Used a nationally representative US sample of 12,791 and eight subjective well-being components. The study reported no robust association between Western zodiac signs and those outcomes; effect sizes explained 0.3% or less of variance. This is limited to the study's sample and outcomes, not every astrological proposition.

## 4. Editorial rules applied to the corpus
1. Classify every claim as astronomical measurement, historical tradition, symbolic reflection or empirical research.
2. Cite official or primary sources for numerical/technical facts.
3. Use original summaries; do not reproduce protected books, tables or article text.
4. Include important study design and limitations alongside headline findings.
5. Keep uncertainty and missingness explicit. Never interpret an absent uncertainty field as zero.
6. Do not convert a chart or symbolic interpretation into a diagnosis, guaranteed event, relationship verdict or investment/medical/legal advice.
