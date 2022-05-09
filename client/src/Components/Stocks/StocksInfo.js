import React, {Component,useEffect } from "react";
import './Stock.css';
import { DataGrid, GridColDef, GridValueGetterParams } from '@mui/x-data-grid';
import axios from "axios";
import {get_quote} from '../../Utils/finance_api'
const columns: GridColDef[] = [
    { field: 'symbol', 
      headerName: 'Symbol', 
      width: 90, 
      headerClassName: 'Header',
     
    },
    { field: 'longName', 
      headerName: 'Name', 
      width: 400, 
      headerClassName: 'Header',
   
    },
    {
      field: 'regularMarketDayHigh',
      headerName: 'High',
      headerClassName: 'Header',
      cellClassName:'High',   
      width: 150,
      editable: true,
    },
    {
      field: 'regularMarketDayLow',
      headerName: 'Low',
      headerClassName: 'Header',
      cellClassName:'Low',      
      width: 150,
      editable: true,
    },
    {
      field: 'regularMarketPrice',
      headerName: 'Price',
      headerClassName: 'Header',   
      width: 150,
      editable: true,
    },
    {
      field: 'regularMarketOpen',
      headerName: 'Market Open',
      headerClassName: 'Header',
     
      width: 150,
      editable: true,
    },
    {
      field: 'regularMarketChange',
      headerName: 'Net Change',
      headerClassName: 'Header',
  
      width: 150,
      editable: true,
    },
    {
      field: 'regularMarketChangePercent',
      headerName: '%Change',
      headerClassName: 'Header',
   
      width: 150,
      editable: true,
    },
    {
      field: 'regularMarketVolume',
      headerName: 'Volumne',
      headerClassName: 'Header',
   
      width: 300,
      editable: true,
    },
  ];
  
  
class StockInfo extends Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      items: [],
      list_code:props.list_code
    };
  }
  async componentDidMount() {
    const {list_code}=this.state
     const res=await get_quote(list_code)
     this.setState({
      items: res.quoteResponse.result,
       isLoaded: true
     })
     console.log(res)    
}
    render(){
      const { error, isLoaded, items, } = this.state;
      for(const item of items){
        if(item.regularMarketChange>0){
          item.status='Green';
        }else{
          item.status='Red'
        }
        item.id=item.symbol;
      }
      console.log(`err ${error}`);
      if(isLoaded){       
        return (
            <div style={{ height: 750, width: '100%' }}>
            <DataGrid
              rows={items}
              columns={columns}
              pageSize={100}
              rowsPerPageOptions={[100]}
              getRowClassName={(params) => params.row.status}             
              disableSelectionOnClick              
            />
          </div>
        )
      }else{
        return(
         <div>API doens't work </div>
        )
      }
    }
}
export default StockInfo;
