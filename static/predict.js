// Function to handle the property area (SemiUrban and Urban)

function handleArea(){
    var semiurban = document.getElementById('property_area_semiurban');
    var urban = document.getElementById('property_area_urban');

    // Disable urban if semiurban is true
    if(semiurban.value == 1){
        urban.disabled = true;
    }
    else{
        urban.disabled = false;
    }
    
    // Disable semiurban if urban is true
    if(urban.value == 1){
        semiurban.disabled = true
    }
    else{
        semiurban.disabled = false;
    }
}

// Function to update the checkboxes
// function updateCheckboxes(prediction){
//     // Accessign the elements

//     var approvedcheckbox = document.getElementById('approvedCheckbox')
//     var disapprovedcheckbox = document.getElementById('disapprovedCheckbox')

//     // Ensure the checkboxes are unticked
//     approvedcheckbox.checked = false
//     disapprovedcheckbox.checked = false

//     // Condition to check prediction value
//     if (prediction === 1){
//         approvedcheckbox.checked = true
//         disapprovedcheckbox.checked = false
//     }
//     else{
//         approvedcheckbox.checked = false
//         disapprovedcheckbox.checked = true
//     }

//     // Disabling the checkboxes to prevent manual entry
//     approvedcheckbox.disabled = true
//     disapprovedcheckbox.disabled = true
// }

// // Fetching the result from Flask
// document.addEventListener("DOMContentLoaded",function() {
//     // Including the prediction variable in Javascript
//     var prediction = "{{ prediction }}";
//     if (prediction.includes("eligible")){
//         updateCheckboxes(1)
//     }
//     else if (prediction.includes("not eligible")){
//         updateCheckboxes(0)
//     }
// });


// Function to clear text displayed on submission of the form
wwindow.onload = function() {
    localStorage.removeItem('disclaimer');  // Clear stored result on page reload
}