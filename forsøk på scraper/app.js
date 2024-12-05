async function dustlooper() {
    let fetching = fetch("https://www.dustloop.com/w/GGST/Anji_Mito/Frame_Data")
    let text = (await fetching).text()
    console.log(text)
    console.log("watersigma")
}
dustlooper()


