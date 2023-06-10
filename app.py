import re


def html_content():
    # Define the HTML content
    html_content = """
  <html>
  <head>
  <title>Our Python Class exam</title>
  
  <style type="text/css">
  	
  	body{
  		width:1000px;
  		margin: auto;
  	}
  	table,tr,td{
  		border:solid;
  		padding: 5px;
  	}
  	table{
  		border-collapse: collapse;
  		width:100%;
  	}
  	h3{
  		font-size: 25px;
  		color:green;
  		text-align: center;
  		margin-top: 100px;
  	}
  	p{
  		font-size: 18px;
  		font-weight: bold;
  	}
  </style>
  
  </head>
  <body>
  <h3>TABLE SHOWING COLOURS OF DRESS BY WORKERS AT BINCOM ICT FOR THE WEEK</h3>
  <table>
  	
  	<thead>
  		<th>DAY</th><th>COLOURS</th>
  	</thead>
  	<tbody>
  	<tr>
  		<td>MONDAY</td>
  		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
  	</tr>
  	<tr>
  		<td>TUESDAY</td>
  		<td>ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE</td>
  	</tr>
  	<tr>
  		<td>WEDNESDAY</td>
  		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE</td>
  	</tr>
  	<tr>
  		<td>THURSDAY</td>
  		<td>BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
  	</tr>
  	<tr>
  		<td>FRIDAY</td>
  		<td>GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE</td>
  	</tr>
  
  	</tbody>
  </table>
  
  <p>Examine the sequence below very well, you will discover that for every 1s that appear 3 times, the output will be one, otherwise the output will be 0.</p>
  <p>0101101011101011011101101000111 <span style="color:orange;">Input</span></p>
  <p>0000000000100000000100000000001 <span style="color:orange;">Output</span></p>
  <p>
  </body>
  </html>
  """

    # Extract dress colors from the HTML table
    pattern = r"<td>([A-Z\s,]+)</td>"
    colors = re.findall(pattern, html_content)

    # Process dress colors for each day
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]

    color_data = dict(zip(days, colors))

    # Print the extracted dress colors
    for day, color in color_data.items():
        print(f"{day}: {color}")

    # Analyze the sequence mentioned in the HTML
    sequence = "0101101011101011011101101000111"
    output = "".join(
        ["1" if sequence[i : i + 3] == "111" else "0" for i in range(len(sequence))]
    )

    # Print the analyzed output sequence
    print(f"Input:  {sequence}")
    print(f"Output: {output}")

    return colors


# html_content()
