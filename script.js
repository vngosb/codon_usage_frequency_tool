$(document).ready(function() {
    $("#dna-form").submit(function(event) {
        event.preventDefault(); // Prevent the default form submission

        var dnaSequence = $("#dna").val(); // Get DNA sequence from the input field

        // Make an AJAX request to the server
        $.ajax({
            type: "POST",
            url: "./final_project.cgi",
            data: { dna: dnaSequence }, // Send the DNA sequence to the server
            dataType: "json", // Expect JSON response
            success: function(response) {
                // Process the JSON response
                var proteinSequence = response.protein_sequence;
                var data = response.data;
		
		// Wrap amino acid sequence
		var wrapLength = 60;
		var wrappedProteinSequence = "";
		for (var i = 0; i < proteinSequence.length; i += wrapLength) {
                    wrappedProteinSequence += proteinSequence.slice(i, i + wrapLength) + "\n";
                }
                // Update the page with the results
                $("#protein-sequence").text("Amino Acid Sequence: " + proteinSequence);

                // Process the 'data' array and update the table using jQuery
                var tableBody = $("#data-table-body");
                tableBody.empty();

                for (var i = 0; i < data.length; i++) {
                    var row = $("<tr>");
                    row.append("<td>" + data[i][0] + "</td>");
                    row.append("<td>" + data[i][1] + "</td>");
                    row.append("<td>" + data[i][2] + "</td>");
                    row.append("<td>" + data[i][3] + "</td>");
                    tableBody.append(row);
                }
            },
            error: function(error) {
                console.error("Error:", error);
            }
        });
    });
});
