# Keep selection editing available during publication

The user twice observed Mark red becoming unavailable during catalogue deployments. The reader compared the global selection-manifest hash with the service response and disabled every color/category control whenever they differed. Reproducing a different service hash against the live reader disabled all 17 visible color buttons. Even an unrelated new card or an added category pair triggered this behavior.

The reader now accepts shared choices across catalogue versions and uses the service’s reported version for compatibility with older backends. A version-only rejection from an older backend receives one automatic retry with the same requested color, category, revision and previous state. Pending saves retain idempotence when a response is lost across publication. The map also keeps reading shared choices when its catalogue hash differs.

The service validates stable IDs, current allowed categories and per-card revisions. Current readers also send the color and category they saw. A mismatch on that card returns the authoritative choice as a conflict, including when an editorial default changed before its first manual edit. A global catalogue hash is no longer an editing lock. Exact successful retries are recognized before stale previous-state checks. Anonymous editing and all notes/proposal/vote authorization remain as before; no runtime secrets or database migrations changed.

Validation passed: all 14 service tests and the production build; the browser selection suite, including version skew in both directions, a lost response across publication, an older service’s version rejection, a fresh visitor during rollout, preserved manual decisions and shared-map updates; the full map browser suite including mobile/offline behavior. Test traffic used isolated SQLite databases. Live verification does not change user selections.

The preceding requested fix also added the natural Algorithms ↔ Graph algorithms pair to TCS-7380. Its down/up operations were checked with both colors in an isolated service, and its live compact/full/mobile button was verified. No shared choice was written for that card.

Already open tabs retain their previous JavaScript until a full reload. One hard refresh is needed to load this fix; subsequent catalogue additions no longer globally disable selection controls in the corrected reader.
