import React from 'react'
import HomeIcon from '@mui/icons-material/Home';
import InsightsIcon from '@mui/icons-material/Insights';
import DashboardIcon from '@mui/icons-material/Dashboard';
export const SidebarData= [
    {
        title:"Home",
        icon:<HomeIcon/>,
        link:"/"
    },
    {
        title:"Analytics",
        icon:<InsightsIcon/>,
        link:"/analytics"
    },
    {
        title:"Dashboard",
        icon:<DashboardIcon/>,
        link:"/dashboard"
    }
]
  