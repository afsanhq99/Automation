describe('Login Tests', () => {
  const url = 'https://practicetestautomation.com/practice-test-login/';

  beforeEach(() => {
    // Visit the login page before each test
    cy.visit("https://practicetestautomation.com/practice-test-login/");
  });

  it('Positive Login Test', () => {
    // Type username and password
    cy.get('#username').type('student');
    cy.get('#password').type('Password123');
    cy.get('#submit').click();

    // Verify the new page URL
    cy.url().should('include', '/logged-in-successfully/');

    // Verify the new page contains expected text
    cy.contains('Congratulations').should('exist');
    cy.contains('successfully logged in').should('exist');

    // Verify the logout button is displayed
    cy.get('.wp-block-button__link.has-text-color.has-background.has-very-dark-gray-background-color')
      .should('be.visible');
  });

  it('Negative Username Test', () => {
    // Type incorrect username and correct password
    cy.get('#username').type('incorrectUser');
    cy.get('#password').type('Password123');
    cy.get('#submit').click();

    // Verify error message is displayed
    cy.get('#error').should('be.visible');

    // Verify error message text
    cy.get('#error').should('have.text', 'Your username is invalid!');
  });

  it('Negative Password Test', () => {
    // Type correct username and incorrect password
    cy.get('#username').type('student');
    cy.get('#password').type('incorrectPassword');
    cy.get('#submit').click();

    // Verify error message is displayed
    cy.get('#error').should('be.visible');

    // Verify error message text
    cy.get('#error').should('have.text', 'Your password is invalid!');
  });
});
