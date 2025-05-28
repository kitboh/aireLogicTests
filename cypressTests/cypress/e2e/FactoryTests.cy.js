import CookiePage from './pom/cookiePage.js';

describe('Factory Test Cases', () => {
  it('Ensure the user can buy a factory and get automatic cookies', () => {
    const cookies = new CookiePage();
    cookies.standardLogin();
    cookies.clickMultipleCookies(21);
    cookies.sellCookies(20);
    cookies.buyFactory(1);
    cy.wait(150); // Wait for page to update. This is bad practice and usually you'd wait on a specific state. There's an external npm package that can help with this, but to save space I'm going to just leave this as is.
    cookies.checkFactoryCount().then((factoryCount) => {
      expect(factoryCount).to.equal('1');
    });
    cy.wait(5100); //There's a bug where you can't sell your last cookie, so we start from 1
    cookies.checkCookieCount().then((cookieCount) => {
      expect(cookieCount).to.equal('6');
    });
  })

  //This one is expected to fail
  it('User cannot buy a factory with no money', () => {
    const cookies = new CookiePage();
    cookies.standardLogin();
    cookies.buyFactory(1);
    cy.wait(150); // Wait for page to update. This is bad practice and usually you'd wait on a specific state. There's an external npm package that can help with this, but to save space I'm going to just leave this as is.
    cookies.checkFactoryCount().then((factoryCount) => {
      expect(factoryCount).to.equal('0');
    });
    cookies.checkMoneyCount().then((moneyCount) => {
      expect(moneyCount).to.equal('0.0');
    });
  })

  it('User can buy multiple factories', () => {
    //I'm just ignoring the bug where you don't need money here
    const cookies = new CookiePage();
    cookies.standardLogin();
    cookies.buyFactory(5);
    cy.wait(150); // Wait for page to update. This is bad practice and usually you'd wait on a specific state. There's an external npm package that can help with this, but to save space I'm going to just leave this as is.
    cookies.checkFactoryCount().then((factoryCount) => {
      expect(factoryCount).to.equal('5');
    });
    cy.wait(5100); //There's a bug where you can't sell your last cookie, so we start from 1
    cookies.checkCookieCount().then((cookieCount) => {
      expect(cookieCount).to.equal('25');
    });
  })
})