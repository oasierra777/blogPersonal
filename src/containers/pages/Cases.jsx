import { useEffect } from "react"

import Header from "components/Cases/Header"
import CasesList from "components/Cases/CasesList"
import Footer from "components/navigation/Footer"
import Navbar from "components/navigation/Navbar"
import Layout from "hocs/layouts/Layout"

function Cases(){

    useEffect(()=>{
        window.scrollTo(0, 0)
    },[])

    return(
        <Layout>
            <Navbar/>
            <div className="pt-28">
                <Header/>
                <CasesList/>
            </div>
            <Footer/>
        </Layout>
    )
}
export default Cases