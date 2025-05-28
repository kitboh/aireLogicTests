import CookiePage from './pom/cookiePage.js';

describe('Basic Test', () => {
  it('Creates a new user and checks the cookie count', () => {
    const cookies = new CookiePage();
    cookies.standardLogin();
    cookies.checkCookieCount().then((cookieCount) => {
      expect(cookieCount).to.equal('0');
    });
  })

  it('Clicks the cookie and checks the count', () => {
    const cookies = new CookiePage();
    cookies.standardLogin();
    cookies.clickCookie();
    cookies.checkCookieCount().then((cookieCount) => {
      expect(cookieCount).to.equal('1');
    });
  })

  it('Clicks the cookie multiple times and checks the count', () => {
    const cookies = new CookiePage();
    cookies.standardLogin();
    cookies.clickMultipleCookies(21);
    cookies.checkCookieCount().then((cookieCount) => {
      expect(cookieCount).to.equal('21');
    });
  })

  it('Shows the correct username', () => {
    const cookies = new CookiePage();
    cookies.standardLogin();
    cy.contains('Hello Test_User')
  })

  it('Has the correct cookie count on the home page', () => {
    const cookies = new CookiePage();
    cookies.standardLogin();
    cookies.clickCookie();
    cookies.returnHome();
    cookies.checkExistingUserScore('Test_User').then((score) => {
      expect(score).to.equal('1');
    });
  })
})