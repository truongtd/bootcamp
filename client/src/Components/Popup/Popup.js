import { Dialog, DialogActions, DialogContent, DialogTitle,Button } from '@mui/material';
import React from 'react'

export default function Popup(props) {
    const {title,children,openPopup,setOpenPopup}=props;
   // const [setOpen] = React.useState(false);
    const handleClose = () => {
        setOpenPopup(false);
      };
  return (
    <Dialog open={openPopup}>
        <DialogTitle>{title}</DialogTitle>
        <DialogContent>{children}</DialogContent>
       
    </Dialog>
  )
}
