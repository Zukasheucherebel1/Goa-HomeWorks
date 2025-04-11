const getElementByIdManual = function(id) {
    // რეკურსიული ძებნა
    function traverse(element) {
        if (element.id === id) {
            return element;
        }
        
        for (let i = 0; i < element.children.length; i++) {
            const found = traverse(element.children[i]);
            if (found) return found;
        }
        
        return null;
    }
    
    return traverse(document.body);
}

const getElementsByClassName = function(className) {
    const elements = [];
    
    // რეკურსიული ძებნა
    function traverse(element) {
        if (element.classList && element.classList.contains(className)) {
            elements.push(element);
        }
        
        for (let i = 0; i < element.children.length; i++) {
            traverse(element.children[i]);
        }
    }
    
    traverse(document.body);
    return elements.length === 1 ? elements[0] : elements;
}

const getElementsByTagName = function(tagName) {
    const elements = [];
    const upperTagName = tagName.toUpperCase();
    
    // რეკურსიული ძებნა
    function traverse(element) {
        if (element.tagName === upperTagName) {
            elements.push(element);
        }
        
        for (let i = 0; i < element.children.length; i++) {
            traverse(element.children[i]);
        }
    }
    
    traverse(document.body);
    return elements.length === 1 ? elements[0] : elements;
}

const manualQuerySelector = function(searchQuery) {
    if (searchQuery[0] === "#") {
        return getElementByIdManual(searchQuery.slice(1));
    } else if (searchQuery[0] === ".") {
        return getElementsByClassName(searchQuery.slice(1));
    } else {
        return getElementsByTagName(searchQuery);
    }
}