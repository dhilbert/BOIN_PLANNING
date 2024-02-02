<?php
include_once('../lib/session.php');
include_once('../lib/dbcon_BOIN_PLANNING.php');

include_once('../contents_header.php');
include_once('../contents_profile.php');
include_once('../contents_sidebar.php');











?>
			<div class="col-sm-9 col-sm-offset-3 col-lg-10 col-lg-offset-2 main">			
					<?php
					$array = array(
						array('#','통합주문관리')
					);
					breadcrumb($array);
					?>
			<div class="row">
			<div class="col-md-12">
				<div class="panel panel-primary">
					<div class="panel-heading">
					
검색 영역					
					</div>

					<div class="panel-body">
					

					












					<div class="col-md-6">
							<form role="form">
							
								<div class="form-group">
									<label>Text Input</label>
									<input class="form-control" placeholder="Placeholder">
								</div>
																
								<div class="form-group">
									<label>Password</label>
									<input type="password" class="form-control">
								</div>
								
								<div class="form-group checkbox">
								  <label>
								    <input type="checkbox">Remember me</label>
								</div>
																
								<div class="form-group">
									<label>File input</label>
									<input type="file">
									 <p class="help-block">Example block-level help text here.</p>
								</div>
								
								<div class="form-group">
									<label>Text area</label>
									<textarea class="form-control" rows="3"></textarea>
								</div>
								
								<label>Validation</label>
								<div class="form-group has-success">
									<input class="form-control" placeholder="Success">
								</div>
								<div class="form-group has-warning">
									<input class="form-control" placeholder="Warning">
								</div>
								<div class="form-group has-error">
									<input class="form-control" placeholder="Error">
								</div>
								
							</div>
							<div class="col-md-6">
							
								<div class="form-group">
									<label>Checkboxes</label>
									<div class="checkbox">
										<label>
											<input type="checkbox" value="">Checkbox 1
										</label>
									</div>
									<div class="checkbox">
										<label>
											<input type="checkbox" value="">Checkbox 2
										</label>
									</div>
									<div class="checkbox">
										<label>
											<input type="checkbox" value="">Checkbox 3
										</label>
									</div>
									<div class="checkbox">
										<label>
											<input type="checkbox" value="">Checkbox 4
										</label>
									</div>
								</div>
								
								<div class="form-group">
									<label>Radio Buttons</label>
									<div class="radio">
										<label>
											<input type="radio" name="optionsRadios" id="optionsRadios1" value="option1" checked>Radio Button 1
										</label>
									</div>
									<div class="radio">
										<label>
											<input type="radio" name="optionsRadios" id="optionsRadios2" value="option2">Radio Button 2
										</label>
									</div>
									<div class="radio">
										<label>
											<input type="radio" name="optionsRadios" id="optionsRadios3" value="option3">Radio Button 3
										</label>
									</div>
									<div class="radio">
										<label>
											<input type="radio" name="optionsRadios" id="optionsRadios3" value="option3">Radio Button 4
										</label>
									</div>
								</div>
								
								<div class="form-group">
									<label>Selects</label>
									<select class="form-control">
										<option>Option 1</option>
										<option>Option 2</option>
										<option>Option 3</option>
										<option>Option 4</option>
									</select>
								</div>
								
								<div class="form-group">
									<label>Multiple Selects</label>
									<select multiple class="form-control">
										<option>Option 1</option>
										<option>Option 2</option>
										<option>Option 3</option>
										<option>Option 4</option>
									</select>
								</div>
								
								<button type="submit" class="btn btn-primary">검색 </button>
								<button type="reset" class="btn btn-default">초기화</button>


					</div>
				</div>
			</div>



		 
  

			<div class="row">
			<div class="col-md-12">
				<div class="panel panel-primary">
					<div class="panel-heading">목록 영역					</div>
					<div class="panel-body">
					<table data-toggle="table" data-url="tables/data1.json"  data-show-refresh="true" data-show-toggle="true" data-show-columns="true" data-search="true" data-select-item-name="toolbar1" data-pagination="true" data-sort-name="name" data-sort-order="desc">
						    <thead>
						    <tr>
						        <th data-field="state" data-checkbox="true" >Item ID</th>
						        <th data-field="id" data-sortable="true">Item ID</th>
						        <th data-field="name"  data-sortable="true">Item Name</th>
						        <th data-field="price" data-sortable="true">Item Price</th>
						    </tr>
						    </thead>
						</table>

					</div>
				</div>
			</div>



		 
	
	</div>
</div>	<!--/.main-->

	
<!--Modal-->
<?php include_once('../contents_footer.php');


?>






