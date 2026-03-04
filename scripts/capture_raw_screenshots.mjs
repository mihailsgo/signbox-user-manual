import { chromium } from "playwright";
import fs from "node:fs";

const USER = process.env.SIGNBOX_USER;
const PASS = process.env.SIGNBOX_PASS;

if (!USER || !PASS) {
  console.error("Missing SIGNBOX_USER or SIGNBOX_PASS environment variables.");
  process.exit(1);
}

const outDir = "assets";
fs.mkdirSync(outDir, { recursive: true });

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function firstVisible(page, selectors) {
  for (const selector of selectors) {
    const loc = selector.startsWith("text=")
      ? page.getByText(selector.slice(5), { exact: false }).first()
      : page.locator(selector).first();
    if ((await loc.count()) > 0) {
      try {
        await loc.waitFor({ state: "visible", timeout: 2000 });
        return loc;
      } catch {
        // continue
      }
    }
  }
  return null;
}

async function clickAny(page, selectors) {
  const loc = await firstVisible(page, selectors);
  if (!loc) return false;
  try {
    await loc.click({ timeout: 5000 });
    return true;
  } catch {
    return false;
  }
}

async function fillAny(page, selectors, value) {
  const loc = await firstVisible(page, selectors);
  if (!loc) return false;
  try {
    await loc.fill(value, { timeout: 5000 });
    return true;
  } catch {
    return false;
  }
}

async function save(page, name) {
  await page.screenshot({ path: `${outDir}/${name}`, fullPage: true });
  console.log(`Saved ${name}`);
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1720, height: 980 } });
const page = await context.newPage();

try {
  await page.goto("https://signbox.trustlynx.com", {
    waitUntil: "domcontentloaded",
    timeout: 120000,
  });
  await sleep(1500);

  await fillAny(page, ['input[name="username"]', '#username', 'input[type="email"]'], USER);
  await fillAny(page, ['input[name="password"]', '#password', 'input[type="password"]'], PASS);
  await clickAny(page, ['button[type="submit"]', "#kc-login", 'input[type="submit"]']);

  await page.waitForLoadState("networkidle", { timeout: 120000 });
  await sleep(2000);
  await save(page, "02-home-create-process.png");

  const candidateFiles = [
    "C:/Repos/trustlynx-infra-tools/fresh_valid_test.pdf",
    "C:/Repos/trustlynx-infra-tools/dl_219c5270-9788-440e-a78a-2fa617d5564e.pdf",
  ].filter((f) => fs.existsSync(f));

  if (candidateFiles.length > 0) {
    const input = page.locator('input[type="file"]').first();
    if ((await input.count()) > 0) {
      await input.setInputFiles(candidateFiles[0]);
      await sleep(2000);
      await save(page, "03-home-after-upload.png");
    }
  }

  await clickAny(page, ['[name="documentType"]', '[id*="documentType"]', "text=Document type"]);
  await sleep(600);
  await save(page, "03-home-after-upload__doctype-open.png");
  await page.keyboard.press("Escape");
  await sleep(200);

  await clickAny(page, ['button:has-text("Add signer")', "text=Add signer"]);
  await sleep(900);
  await save(page, "04-recipient-fields.png");

  await clickAny(page, ['select[name*="country"]', '[name*="country"]', "text=Country"]);
  await sleep(500);
  await save(page, "04-recipient-fields__country-open.png");
  await page.keyboard.press("Escape");
  await sleep(200);

  await clickAny(page, ['button:has-text("Select contact")', "text=Select contact"]);
  await sleep(900);
  await save(page, "04-recipient-fields__select-contact-open.png");
  await page.keyboard.press("Escape");
  await sleep(200);

  await clickAny(page, ['button:has-text("Select template")', "text=Select template"]);
  await sleep(900);
  await save(page, "03-home-after-upload__template-open.png");
  await page.keyboard.press("Escape");
  await sleep(200);

  await clickAny(page, ['a:has-text("History")', "text=History"]);
  await page.waitForLoadState("networkidle", { timeout: 120000 });
  await sleep(1200);
  await save(page, "05-history-filters.png");

  await clickAny(page, ['[name="status"]', "text=Status"]);
  await sleep(500);
  await save(page, "05-history-filters__status-open.png");
  await page.keyboard.press("Escape");
  await sleep(200);

  await page.goto("https://esign.trustlynx.com", {
    waitUntil: "domcontentloaded",
    timeout: 120000,
  });
  await sleep(1500);
  await save(page, "08-external-portal.png");

  console.log("Raw screenshot capture complete.");
} finally {
  await browser.close();
}
