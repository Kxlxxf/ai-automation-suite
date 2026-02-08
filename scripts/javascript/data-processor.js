'use strict';

/**
 * Data Processor Module
 * This module provides functionality for data processing and transformation.
 */

class DataProcessor {
    constructor(data) {
        this.data = data;
    }

    // Method to filter data based on a condition
    filter(condition) {
        return this.data.filter(condition);
    }

    // Method to map data to a new format
    map(transform) {
        return this.data.map(transform);
    }

    // Method to reduce data to a single value
    reduce(reducer, initialValue) {
        return this.data.reduce(reducer, initialValue);
    }

    // Method to transform the data using a provided function
    transform(transformFunction) {
        this.data = transformFunction(this.data);
        return this.data;
    }
}

// Usage Example:
// const dataProcessor = new DataProcessor([1, 2, 3, 4, 5]);
// const filteredData = dataProcessor.filter(num => num > 2);
// const mappedData = dataProcessor.map(num => num * 2);
// const reducedData = dataProcessor.reduce((acc, num) => acc + num, 0);

module.exports = DataProcessor;
