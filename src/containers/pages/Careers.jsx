import { useEffect } from "react"

import Footer from "components/navigation/Footer"
import Navbar from "components/navigation/Navbar"
import Layout from "hocs/layouts/Layout"
import Header from "components/careers/Header"
import Testimonial from "components/careers/Testimonials"
import PositionsList from "components/careers/PositionsList"
import Features from "components/careers/Features"

function Careers(){

    useEffect(()=>{
        window.scrollTo(0, 0)
    },[])

    return(
        <Layout>
            <Navbar/>
            <div className="pt-28">
                <Header/>
                <Testimonial/>
                <PositionsList/>
                <Features/>
            </div>
            <Footer/>
        </Layout>
    )
}
export default Careers