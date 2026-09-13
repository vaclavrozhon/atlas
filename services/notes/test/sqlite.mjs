import {DatabaseSync} from 'node:sqlite';

// Execute the production worker's SQL against real SQLite in local tests.
export function database(path = ':memory:') {
  const db = new DatabaseSync(path);
  const prepare = (sql, args = []) => ({
    bind: (...values) => prepare(sql, values),
    async first() { return db.prepare(sql).get(...args) || null; },
    async all() { return {results: db.prepare(sql).all(...args)}; },
    async run() { return db.prepare(sql).run(...args); },
  });
  return {
    prepare,
    async batch(statements) {
      db.exec('BEGIN');
      try { const results = []; for (const statement of statements) results.push(await statement.run()); db.exec('COMMIT'); return results; }
      catch (error) { db.exec('ROLLBACK'); throw error; }
    },
    close() { db.close(); },
  };
}
