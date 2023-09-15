import { useEffect } from "react"


import Header from "components/Home/Header"
import Incentives from "components/Home/Incentives"
import UseCases from "components/Home/UseCases"
import Features from "components/Home/Features"
import CTA from "components/Home/CTA"
import LogoCloud from "components/Home/LogoCloud"
import BlogList from "components/Home/BlogList"
import Footer from "components/navigation/Footer"
import Navbar from "components/navigation/Navbar"
import Layout from "hocs/layouts/Layout"

function Home(){

    useEffect(()=>{
        window.scrollTo(0, 0)
    },[])
    
    return(
        <Layout>
            <Navbar/>
            <div className="pt-28">
                <Header/>
                <Incentives/>
                <UseCases/>
                <Features/>
                <CTA/>
                <LogoCloud/>
                <BlogList/>
            </div>
            <Footer/>
        </Layout>
    )
}
export default Home