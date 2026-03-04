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

async function save(page, name, fullPage = true) {
  await page.screenshot({ path: `${outDir}/${name}`, fullPage });
  console.log(`Saved ${name}`);
}

async function clickIfVisible(page, selector) {
  const loc = page.locator(selector).first();
  if ((await loc.count()) === 0) return false;
  try {
    await loc.click({ timeout: 4000 });
    return true;
  } catch {
    return false;
  }
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1720, height: 980 } });
const page = await context.newPage();

try {
  await page.goto("https://signbox.trustlynx.com", {
    waitUntil: "domcontentloaded",
    timeout: 120000,
  });
  await sleep(1200);

  const userInput = page.locator('input[name="username"], #username, input[type="email"]').first();
  if ((await userInput.count()) === 0) {
    await clickIfVisible(page, 'button:has-text("Login")');
    await sleep(1200);
  }
  await userInput.waitFor({ state: "visible", timeout: 30000 });
  await save(page, "01-login-page.png", false);

  await page.fill('input[name="username"], #username, input[type="email"]', USER);
  await page.fill('input[name="password"], #password, input[type="password"]', PASS);
  await page.click('button[type="submit"], #kc-login, input[type="submit"]');
  await page.waitForLoadState("networkidle", { timeout: 120000 });
  await sleep(1300);

  await save(page, "02-home-create-process.png");

  const candidates = [
    "C:/Repos/trustlynx-infra-tools/fresh_valid_test.pdf",
    "C:/Repos/trustlynx-infra-tools/dl_219c5270-9788-440e-a78a-2fa617d5564e.pdf",
  ].filter((f) => fs.existsSync(f));

  if (candidates.length > 0) {
    const fileInput = page.locator('input[type="file"]').first();
    if ((await fileInput.count()) > 0) {
      await fileInput.setInputFiles(candidates[0]);
      await sleep(1800);
    }
  }

  await page.click("#documentType");
  await sleep(250);
  await save(page, "03-home-after-upload__doctype-open.png", false);
  await page.keyboard.press("Escape");
  await sleep(200);

  await page.click('button:has-text("Select template")');
  await sleep(550);
  await save(page, "03-home-after-upload__template-open.png", false);
  await page.keyboard.press("Escape");
  await sleep(200);

  await page.click('button:has-text("Add signer")');
  await sleep(600);
  await save(page, "04-recipient-fields.png");

  await page.locator('[id="groups.0.signers.0.country"]').click();
  await sleep(250);
  await save(page, "04-recipient-fields__country-open.png", false);
  await page.keyboard.press("Escape");
  await sleep(200);

  await page.click('button:has-text("Select contact")');
  await sleep(700);
  await save(page, "04-recipient-fields__select-contact-open.png", false);
  await page.keyboard.press("Escape");
  await sleep(200);

  await page.click("text=History");
  await page.waitForLoadState("networkidle", { timeout: 120000 });
  await sleep(800);
  await save(page, "05-history-filters.png");

  await page.click("#status");
  await sleep(300);
  await save(page, "05-history-filters__status-open.png", false);
  await page.keyboard.press("Escape");
  await sleep(200);

  const firstRow = page.locator("table tbody tr").first();
  if ((await firstRow.count()) > 0) {
    await firstRow.click();
    await page.waitForLoadState("networkidle", { timeout: 120000 });
    await sleep(900);
    await save(page, "13-process-detail.png");
  }

  await page.goto("https://esign.trustlynx.com", {
    waitUntil: "domcontentloaded",
    timeout: 120000,
  });
  await sleep(1200);
  await save(page, "08-external-portal.png", false);

  console.log("Raw screenshot capture complete.");
} finally {
  await browser.close();
}
