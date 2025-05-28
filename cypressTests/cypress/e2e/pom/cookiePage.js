import HomePage from './homePage.js';

class CookiePage extends HomePage {
    returnHome() {
        cy.get('a').contains('Cookie Clicker!').click();
    }
    clickCookie() {
        cy.get('#click').click();
    }
    clickMultipleCookies(integer) {
        for (let i = 0; i < integer; i++) {
            cy.get('#click').click();
        }
    }
    checkCookieCount() {
        return cy.get('#cookies').invoke('text');
    }
    checkFactoryCount() {
        return cy.get('#factories').invoke('text');
    }
    checkMoneyCount() {
        return cy.get('#money').invoke('text');
    }

    buyFactory(amount) {
        cy.get('#factories-to-buy').click().type(amount);
        cy.get('#buy-factories').click();
    }

    sellCookies(amount) {
        cy.get('#cookies-to-sell').click().type(amount);
        cy.get('#sell-cookies').click();
    }
}

export default CookiePage;