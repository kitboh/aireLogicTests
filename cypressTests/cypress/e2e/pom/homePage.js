class HomePage {
    visit() {
      cy.visit('/');
      Cypress.on('uncaught:exception', (err, runnable) => {
        // returning false here prevents Cypress from
        // failing the test
        return false
    })
    }
  
    nameEntry(username) {
        cy.get('input[name="name"]').click().type(username);
    }

    submitEntry() {
        cy.get('button').contains('Start!').click();
    }

    clickExistingUser(username) {
        cy.get('a').contains(username).click();
    }

    checkExistingUserScore(username) {
        // This returns the score of a specific user
        return cy.get('a').contains(username).parent('td').next('td').invoke('text');
    }

    standardLogin(){
        // This is the standard login for the test user
        this.visit();
        this.nameEntry('Test_User');
        this.submitEntry();
    }
  }
  
  export default HomePage;