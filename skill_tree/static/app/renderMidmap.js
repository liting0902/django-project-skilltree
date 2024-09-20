let url = new URL(window.location.href);

async function getFetch(url) {
  try {
    const getRes = await new Promise((resolve, reject) => {
      fetch(url, {
        method: "GET",
      }).then((res) => {
        resolve(res.json());
      });
    });
    return getRes;
  } catch (error) {
    console.log(error);
  }
}

async function getData() {
  let fetchedData = await getFetch(
    `./api/skillsList/?category=${url.searchParams.get(
      "category"
    )}&&format=json`
  );
  const transKey = fetchedData.map((item) => ({
    ...item,
    "background-color": item["background_color"],
  }));
  await load_jsmind(transKey);
}

getData();

let arrayColorNodes = [];

function colorMind(list_MindData) {
  arrayColorNodes = list_MindData.filter((item) => {
    return item["background-color"]; //not null
  });
  list_MindData.forEach((itemChild) => {
    if (itemChild["background-color"]) return;
    if (itemChild.notuse) {
      switch (itemChild.notuse) {
        case 1: // learened
          itemChild["background-color"] = "#888888"; //888888
          break;
        case 2: // can't do it
          itemChild["background-color"] = "#888888"; //CCCCCC
          break;
        default:
          itemChild["background-color"] = "#CCCCCC";
          break;
      }
      return;
    }
    let foundParent = arrayColorNodes.find((itemParent) => {
      return itemParent.id === itemChild.parentid;
    });
    // possible undefined
    if (foundParent) {
      itemChild["background-color"] = foundParent["background-color"];
      itemChild["foreground-color"] = foundParent["foreground-color"];
    }
  });
  return list_MindData;
}

async function load_jsmind(mData) {
  let mind = {
    format: "node_array",
    data: mData,
  };

  let list_ColorData = await colorMind(mind.data);
  list_ColorData = await colorMind(mind.data);
  list_ColorData = await colorMind(mind.data);

  mind.data = await list_ColorData;
  var options = {
    container: "jsmind_container",
    editable: true,
    theme: "primary",
    view: {
      engine: "canvas",
    },
  };
  jsMind.show(options, mind);
}
