$(document).ready(function() {
	/*$(".tank-selector").select2({
		placeholder: "Select a tank",
		allowClear: true
	});	*/
	
	$("#player-amount").select2();
});

function setPlayers(){	
	//create form
	originalBody = $("body").html();
	
	//create the table
	var string = '<form action="scrape.py" method="GET"><div id="tank-table-container"><table id="tank-table">';
	
	for (var i = 0; i < $("#player-amount").select2("val"); i++){
		console.log("Passed");
		string += `<tr>
				<td><select class="tank-selector" id="tank-selector-` + i + '" name="tank' + (i + 1) + `">
					<option></option>
					<optgroup label="America">
						<option>T92</option>
						<option>XM551 Sheridan</option>
						<option>T57 Heavy</option>
						<option>T110E4</option>
						<option>T110E3</option>
						<option>M48A5 Patton</option>
						<option>T110E5</option>
					</optgroup>
					<optgroup label="Germany">
						<option>GW E 100</option>
						<option>G121 Grille 15 L63</option>
						<option>JagdPz E-100</option>
						<option>Pz.Kpfw. VII</option>
						<option>Maus</option>
						<option>E-100</option>
						<option>E-50 Ausf. M</option>
						<option>Leopard 1</option>
						<option>Rheinmetall Panzerwagen</option>
					</optgroup>
					<optgroup label="USSR">
						<option>Object 268</option>
						<option>Object 263</option>
						<option>T-100 LT</option>
						<option>T62A</option>
						<option>Object 140</option>
						<option>Object 430</option>
						<option>IS-7</option>
						<option>IS-4</option>
						<option>Object 261</option>
						<option>Object 907</option>
						<option>Object 260</option>
					</optgroup>
					<optgroup label="Britain">
						<option>Centurion Action X</option>
						<option>Badger</option>
						<option>Super Conqueror</option>
						<option>FV4005 Stage II</option>
						<option>Conqueror Gun Carriage</option>
					</optgroup>
					<optgroup label="France">
						<option>AMX 50 Foch B</option>
						<option>AMX M4 Mle 54 </option>
						<option>AMX 50B</option>
						<option>Bat Chatillon 25 t</option>
						<option>AMX 13 105</option>
						<option>AMX 30B</option>
						<option>Bat Chatillon 155</option>
					</optgroup>
					<optgroup label="Czechoslovakia">
						<option>T50 51</option>
					</optgroup>
					<optgroup label="Japan">
						<option>STB-1</option>
						<option>Type 5 Heavy</option>
					</optgroup>
					<optgroup label="China">
						<option>WZ-113G FT</option>
						<option>WZ-132-1</option>
						<option>121</option>
						<option>WZ-111 model 5A</option>
						<option>113</option>
					</optgroup>
					<optgroup label="Sweden">
						<option>Strv 103B</option>
						<option>Kranvagn</option>
					</optgroup>
				</select></td>
			</tr>`;
	}
	
	string += "</table></div>";
	
	//create the player box
	string += '<div id="player-box-container"><input type="text" name="names" id="player-box"></input><input type="submit" value="Create" id="player-box-button"></input></div></form>';
	$("body").html(originalBody + string);
	
	for (var i = 0; i < $("#player-amount").select2("val"); i++){
		$("#tank-selector-" + i).select2({
			placeholder: "Select a tank",
			allowClear: true
		});
	}
	
}