import { useEffect } from "react"

import Footer from "components/navigation/Footer"
import Navbar from "components/navigation/Navbar"
import Layout from "hocs/layouts/Layout"
import Header from "components/About/Header"
import TestStats from "components/About/TestSatats"
import Images from "components/About/Image"
import Clients from "components/About/Clients"
import Features from "components/About/Features"
import Team from "components/About/Teams"

function About(){

    useEffect(()=>{
        window.scrollTo(0, 0)
    },[])

    return(
        <Layout>
            <Navbar/>
            <div className="pt-28">
                <Header/>
                <TestStats/>
                <Images/>
                <Clients/>
                <Features/>
                <Team/>
            </div>
            <Footer/>
        </Layout>
    )
}
export default About