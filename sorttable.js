function sortTable(colIndex, columnElement, isNumeric = false) {
  var table, rows, switching, i, x, y, shouldSwitch, sortOrder;
  // table = document.getElementById("myTable");
  table = columnElement.parentElement.parentElement.parentElement;
  switching = true;
  
  //remove existing up/down arrow in any column
  sortfwdind = document.getElementById('sorttable_sortfwdind');
  if (sortfwdind) { sortfwdind.parentNode.removeChild(sortfwdind); }
  sortrevind = document.getElementById('sorttable_sortrevind');
  if (sortrevind) { sortrevind.parentNode.removeChild(sortrevind); }
  
  //decide whether to be ascending or descending
  if (columnElement.className === "asc") {
    //column is already ascending so make it descending
    sortOrder = "desc"
    columnElement.className = "desc"

    sortrevind = document.createElement('span');
    sortrevind.id = "sorttable_sortrevind";
    sortrevind.innerHTML = '&nbsp;&#x25B4;';
    columnElement.appendChild(sortrevind);
  } else {
    //column is already descending or isn't sorted so make it ascending
    sortOrder = "asc"
    columnElement.className = "asc"

    sortfwdind = document.createElement('span');
    sortfwdind.id = "sorttable_sortfwdind";
    sortfwdind.innerHTML = '&nbsp;&#x25BE;';
    columnElement.appendChild(sortfwdind);
  }
  //reset all other column asc/desc changes
  columnHeads = columnElement.parentElement.children
  for(var i = 0; i < columnHeads.length; i++) {
    if (columnHeads[i] === columnElement) {
      //skip current column
      continue;
    }
    columnHeads[i].className = "";
  }

  while (switching) {
    switching = false;
    rows = table.rows;
    for (i = 1; i < (rows.length - 1); i++) {
      shouldSwitch = false;
      x = rows[i].getElementsByTagName("td")[colIndex];
      y = rows[i + 1].getElementsByTagName("td")[colIndex];
      if (isNumeric) {
        //column should be treated as numeric
        x = parseFloat(x.innerHTML)
        y = parseFloat(y.innerHTML)
        if (sortOrder === "asc") {
          if (x > y) {
            shouldSwitch = true;
            break;
          }
        } else if (sortOrder === "desc") {
          if (x < y) {
            shouldSwitch = true;
            break;
          }
        }
      }
      else{
        //column should be treated as string
        if (sortOrder === "asc") {
          if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
            shouldSwitch = true;
            break;
          }
        } else if (sortOrder === "desc") {
          if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
            shouldSwitch = true;
            break;
          }
        }
      }
      
    }
    if (shouldSwitch) {
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
    } else {
      if (sortOrder === "asc") {
        sortOrder = "desc";
      } else {
        sortOrder = "asc";
      }
    }
  }
}