import { addCypressConfig } from '@cypress/config';
import path from 'path';

addCypressConfig({
    // Add the .js extension to the file extensions
    fileExtensions: ['js'],
});